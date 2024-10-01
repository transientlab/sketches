use ipnetwork::IpNetwork;
use std::net::{IpAddr, SocketAddr};
use std::pin;
use tokio::net::TcpStream;
use tokio::time::{timeout, Duration};
use get_if_addrs::get_if_addrs;
use std::error::Error;
use ping::ping;

const TIMEOUT: u64 = 10;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // Retrieve and print the IP address of the network interface
    let local_ip = get_local_ip()?;
    println!("Local IP address: {}", local_ip);

    // Define the subnet to scan based on the local IP
    let subnet: IpNetwork = match local_ip {
        IpAddr::V4(ipv4) => IpNetwork::new(IpAddr::V4(ipv4), 24)?,
        IpAddr::V6(_) => {
            println!("IPv6 is not supported in this example.");
            return Ok(());
        }
    };
    println!("----\n{} scanning subnet", subnet);
    // Iterate over all possible IPs in the subnet
    for ip in subnet.iter() {
        if ping_ip(ip).await {
            println!("----\n{}", ip);
            println!("ping response received");
        }
        let socket_addr = SocketAddr::new(ip, 80);
        if check_ip(socket_addr).await {
            println!("web server response received");
        }
    }
    println!("----\nEND");
    Ok(())
}

async fn check_ip(addr: SocketAddr) -> bool {
    // Set a timeout for the connection attempt
    match tokio::time::timeout(Duration::from_millis(TIMEOUT), TcpStream::connect(&addr)).await {
        Ok(Ok(_)) => true,  // Connection was successful
        _ => false,         // Connection failed or timed out
    }
}

async fn ping_ip(ip: IpAddr) -> bool {
    // Send a ping to the IP address
    let payload: [u8; 24] = [0; 24];

    match tokio::time::timeout(
        Duration::from_millis(TIMEOUT), 
        {
            smol_ping::AsyncPinger::new().expect("Failed to create AsyncPinger");

        })
        ).await {
            Ok(Ok(_)) => true,
            _ => false,
        }
    
    // match tokio::task::spawn_blocking(move || {
    //         let status = ping(ip, Some(Duration::from_millis(TIMEOUT)), None, None, None, Some(&payload));
    //         // println!("{:#?}", status);
    //         match status {
    //             Ok(_) => true,
    //             _ => false,
    //         }
    //         }
    //     ).await {
    //     Ok(true) => true,
    //     _ => false,
    // }
}

fn get_local_ip() -> Result<IpAddr, Box<dyn Error>> {
    let if_addrs = get_if_addrs()?;
    for if_addr in if_addrs {
        // Filter out non-IPv4 addresses and loopback addresses
        if let IpAddr::V4(ipv4) = if_addr.addr.ip() {
            if !ipv4.is_loopback() {
                return Ok(IpAddr::V4(ipv4));
            }
        }
    }
    Err("No suitable IPv4 address found.".into())
}

/*
use plotters::prelude::*;

fn main() {
    // Create a drawing area on a bitmap
    let root_area = BitMapBackend::new("chart.png", (800, 600))
        .into_drawing_area();
    root_area.fill(&WHITE).unwrap();

    // Create a chart builder
    let mut chart = ChartBuilder::on(&root_area)
        .caption("Simple Line Chart", ("sans-serif", 50).into_font())
        .margin(10)
        .x_label_area_size(30)
        .y_label_area_size(30)
        .build_cartesian_2d(0..10, 0..10)
        .unwrap();

    // Configure the mesh (grid and axis labels)
    chart.configure_mesh().draw().unwrap();

    // Plot a line series
    chart
        .draw_series(LineSeries::new(
            (0..100).map(|x| (x, x * x)),
            &RED,
        ))
        .unwrap()
        .label("y = x^2")
        .legend(|(x, y)| PathElement::new(vec![(x, y), (x + 20, y)], &RED));

    // Add a legend
    chart.configure_series_labels()
        .background_style(&WHITE.mix(0.8))
        .border_style(&BLACK)
        .draw()
        .unwrap();
}


--------------------------------------------------------------------

use std;

fn main() -> std::result::Result<T, E>{
    let _lista = vec![1,2,3];
    let resulte = assert_eq!(_lista[0], 1);
    println!("{:?}", resulte);
}


use cpal::{
    traits::{DeviceTrait, HostTrait, StreamTrait},
    FromSample, Sample, SizedSample,
};
use std::{f32::consts::PI, time::Duration};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Set up the audio host and device
    let host = cpal::default_host();
    let device = host.default_output_device().expect("Failed to find a default output device.");
    let config = device.default_output_config()?.config();

    // Create the sine wave generator
    let sample_rate = config.sample_rate.0 as f32;
    let mut sample_clock = 0f32;
    let freq = 440.0; // Frequency of the sine wave (A4)

    // Define the next value function for the sine wave
    let next_value = move || {
        sample_clock = (sample_clock + 1.0) % sample_rate;
        (2.0 * PI * freq * (sample_clock / sample_rate)).sin()
    };

    // Create and run the audio stream
    let stream = run::<f32>(&device, &config, next_value);

    println!("Playing sound for 3 seconds...");
    std::thread::sleep(std::time::Duration::from_secs(3));
    drop(stream); // Stop the stream after 3 seconds

    Ok(())
}

fn run<T>(device: &cpal::Device, config: &cpal::StreamConfig, mut next_value: impl FnMut() -> f32 + Send + 'static) -> Result<cpal::Stream, Box<dyn std::error::Error>>
where
    T: Sample,
    T: SizedSample + FromSample<f32>,
{
    let err_fn = |err| eprintln!("An error occurred on the output audio stream: {}", err);
    let dur : Option<Duration> = std::time::Duration::new(3, 0);
    let stream = device.build_output_stream(
        config,
        move |data: &mut [T], _: &cpal::OutputCallbackInfo| {
            write_data(data, &mut next_value)
        },
        err_fn,
        dur,
    )?;

    stream.play()?;
    Ok(stream)
}

fn write_data<T>(output: &mut [T], next_value: &mut impl FnMut() -> f32)
where
    T: cpal::Sample,
{
    let
    for sample in output.iter_mut() {
        let value: f32 = next_value();
        *sample = <dyn cpal::Sample>::from(&value);
    }



}

use std::{
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
        .lines()
        .map(|result| result.unwrap())
        .take_while(|line| !line.is_empty())
        .collect();

    println!("Request: {http_request:#?}");
}



use std::net::TcpListener;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        println!("Connection established!");
    }
}


// use std::io;
// use rand::Rng;
// use std::cmp::Ordering;
// use std::net;
use mini_redis::{client, Result};

#[tokio::main]
async fn main() -> Result<()> {
    // Open a connection to the mini-redis address.
    let mut client = client::connect("127.0.0.1:6379").await?;

    // Set the key "hello" with value "world"
    client.set("siemano", "witamy".into()).await?;
    client.set("hello", "world".into()).await?;
    
    // Get key "hello"
    let result = client.get("hello").await?;

    
    println!("got value from the server; result={:?}", result);

    Ok(())
}

fn main() {
}

fn guess_game() {
    let secret = rand::thread_rng().gen_range(0..=100);
    loop {
        println!("podaj dowolną liczbę");
        let mut guess = String::new();
        io::stdin()
            .read_line(&mut guess)
            .expect("failed to readline");

        let guess : u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        match guess.cmp(&secret) {
            Ordering::Greater => println!("mniejszą"),
            Ordering::Less => println!("większą"),
            Ordering::Equal => {
                println!("o to to, taką taką");
                break;
            }
        }
    }
}

fn arridx() {
    let a = [1, 2, 3, 4, 5];

    println!("Please enter an array index.");

    let mut index = String::new();

    io::stdin()
        .read_line(&mut index)
        .expect("Failed to read line");

    let index: usize = index
        .trim()
        .parse()
        .expect("Index entered was not a number");

    let element = a[index];

    println!("The value of the element at index {index} is: {element}");
}

fn conn() {
    let localhost = net::Ipv4Addr::new(127, 0, 0, 1);
    let server = net::Ipv4Addr::new(174, 128, 0, 1);
    
}

 */