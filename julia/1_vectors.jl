x = [1.1, 0.0, 3.2, -3.1]
y = [1.2; 3.2; 6.3; -7.2]

l_x = length(x)
l_y = length(y)

print(l_x)

print(x[3])

print(y)

x[3] = 5
y[2] = 4
print(x[end])

# assignment vs copying
y = x       # new reference for x array
            # from now on y points to the same memory region as x

y = copy(x) # creates new memory allocation

# vector equality, scalars
x == y
# x=1.2, y[1]=1.2        ->   x != y      !!!

# concatenation, block, stacked vectors
z = [x; y]
z = vcat(x, y)

# tuple
z = (x, y)

# array
z = [x, y]

# slicing, subvectors
x[4:5] = [1, 2]
z[end:-2:1]     # step 2, backwards

# vector of first differences
x = [1, 2, 3, 0, 3, 7, 9]
d = x[2:end] - x[1:end-1]

# list of vectors
list = [x, y, z]        # 1 dimensional array of vectors
list = (x, y, z)        # tuple or list

# zero vectors
u = zeros(3)            # 3 elements zero vector

# unit vectors
n = 4, i = 2
ei = zeros(n)
ei[i] = 1
unit_vector(i, n) = [zeros(i-1); 1; zeros(n-i)]

# ones
ones(n)

# random
rand(n)
randn(n)        # normal distribution

# vector addition
x + y
x - y

# scalars
x / 3 = 3 \ x = x ./ 3                   # != 3 / x
3 * x = x * 3 = x .* 3
x .+ 3              # apply +3 to all vector elements
x .- 3

# elementwise operations
x ./ y

# elementwise with scalars
x .^ a              # gives a vector  {x[i]^a, ...}

# elementwise function application     function.(x)
sin.(x)     # returns vector of {sin(x[i]), ... }
x .== y     # returns bit vector
x[2:3] .= 1.3

# inner product
x'*y  

# vector of differences
diff_v = [x[i+1] - x[i] for i = 1:length(x)-1]
diff_v = [x[2:length(x)] - x[1:length(x)-1]]

# boolean vector encoding  transformation
u = [0, 1, 1, 0]
r = 2 .* u - ones(length(u))

