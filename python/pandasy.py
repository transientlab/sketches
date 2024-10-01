import csv, json, ldif
import os, re, pandas as pd

# dane wejściowe
wd = os.getcwd()
data_folder = 'dane'
file_extensions = ['csv', 'json', 'ldif'] # must define read_$EXTENSION function for each
entry_columns = ['Customer', 'Country', 'Order', 'Status', 'Group']

# 1
# odczyt pliku według formatu
def read_csv(file_path):
    csv_data = []
    with open(file_path, 'r') as csv_file_handle:
        csv_file = csv.reader(csv_file_handle, delimiter='|')
        for i in csv_file:
            csv_data.append(i)
    return csv_data[1:]
def read_json(file_path):
    json_data = []
    with open(file_path, 'r') as json_file_handle:
        json_file = json.load(json_file_handle)
        for row in json_file['data']:
            json_data.append(row)
    return json_data
def read_ldif(file_path):
    with open(file_path, 'r') as ldif_file_handle:
        ldif_data = ''
        for i in ldif_file_handle:
            ldif_data += i
        entries = re.split(r'\n\s*\n', ldif_data.strip())

        parsed_data = []
        for entry in entries:
            elements = re.findall(r'(\w+):(.+)', entry)
            parsed_entry = [value.strip() for _, value in elements]
            parsed_data.append(parsed_entry)
    return parsed_data

def x_read_all(data_folder=data_folder, file_extensions=file_extensions, entry_coulmns=entry_columns):
    dataframes = []
    all_df = pd.DataFrame()
    for file in os.listdir(os.path.join(wd, data_folder)):
        for extension in file_extensions:
            if file.endswith(extension):
                array = globals()['read_' + extension](os.path.join(wd, data_folder, file))
                df = pd.DataFrame(array, columns=entry_columns)
                dataframes.append({'filename': file, 'df' : df})
                # spajanie wszystkich spisów do jednej tabeli
                all_df = pd.concat([all_df, df], ignore_index=True)
    return all_df, dataframes

# 2
def count_top_orders(all_df, top_count):
    # znajdź najczęstsze wystąpienia i zwróć wybraną ilość
    order_counts = all_df['Order'].value_counts()[:top_count]
    return order_counts

# 3
def top_countries_in_groups(all_orders):
    # znajdź listę wystąpień w kolumnie grup
    groups = all_orders.Group.unique()
    top_countries = []
    for group in groups:
        if group == None:
            continue
        # wybierz daną grupę z tabeli
        df1 = all_orders[all_orders['Group'] == group]
        # zlicz wystąpienia państw w grupie
        all_counts = df1['Country'].value_counts()
        # znajdź najwyższą wartość
        max_counts = all_counts.max()
        # wybierz wszystkie o największej liczbie wartości
        most_frequent_countries = all_counts[all_counts == max_counts]
        countries = []
        # wypisz indeksy do tabeli i zgrupuj wyniki dotyczące grupy
        for j in most_frequent_countries.index:
            countries.append(j)
        top_countries.append([group, max_counts, countries])
    return sorted(top_countries, key=lambda x: x[0])

# 4
# ? find_status_max można połączyć z count_top_orders
def find_status_max(df, key=None):
    status_count = df['Status'].value_counts()
    return status_count
def top_status_files(dataframes):
        # stwórz nową tabelę
        statuses_df = pd.DataFrame()
        # po tabelach w zależności od pliku
        for chunk in dataframes:
            extension = chunk['filename'].split('.')[1]
            # dołączaj kolejno kolumnę z  wystąpieniami i tytułuj tą kolumnę rozszerzeniem pliku
            statuses_df = pd.concat([statuses_df, find_status_max(chunk['df']).to_frame(name=extension)], axis=1)
        # znajdź wszystkie statusy
        statuses = all_df.Status.unique()
        # transponuj tabelę
        dfa = statuses_df.transpose()
        # znajdź największe
        vals = dfa.max()
        top_status = []
        # po statusie wynajduj listę typów plików
        for status in statuses:
            # dla wybranego statusu
            dfb = dfa[dfa == vals[status]]
            # znajdź listę indeksów z najczęstszym wystąpieniem
            file_types = dfb[dfb[status] == vals[status]].index.tolist()
            # zbierz to tabeli wyników
            top_status.append([status, vals[status], file_types])
        return top_status

# 5
def count_consonants(all_df):
        count = 0
        letters = 'qwrtpsdfghjklzxcvbnm'
        # po każdej wartości w nazwie klienta
        for i in all_df.Customer:
            # po każdym jej znaku
            for j in i.lower():
                # sprawdź czy występuje
                if j in letters:
                    count += 1
        return count


if __name__ == '__main__':

    # 1
    all_df, dataframes = x_read_all()

    # 2
    most_ordered = count_top_orders(all_df, 30)
    
    # 3
    cntry_grps = top_countries_in_groups(all_df)

    #4 
    top_files = top_status_files(dataframes)

    # 5 
    consonants_count = count_consonants(all_df)

    # generate HTML page
    html_preamble = '''
<!DOCTYPE html>
<html>
    <head>
        <title>data report</title>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        
    </head>
    <style>
body{line-height:1;columns:auto;text-align:left;background-color:#aabbaa;min-width:610px;max-width:610px;margin-right:20px;margin-left:20px;margin-top:20px;width:96%;font-size:large;
font-family:'CourierNew',Courier,monospace;font-weight:bold;}table{border-collapse:separate;border-spacing:1px;border-width:5px;border-color:#99aa99;border-style:ridge;width:600px;
margin:0px;}tr.head{color:#ff3344;border-collapse:separate;border-spacing:1px;border-width:1px;border-color:#ffffff;border-style:solid;background-color:#ffffff;}td{padding:2px;
border-collapse:separate;border-spacing:1px;border-width:1px;border-color:#777777;border-style:solid;}div{position:relative;color:#443322;font-family:'CourierNew',Courier,monospace;font-size:16px;}
    </style>
    <body>
                    '''    
    with open('index.html', 'w+') as file:
        file.write(html_preamble)

        html_chunk = '\n<div id=\"mst\"><table><tr class=\"head\">'
        for i in ['NAZWA LEKU', 'LICZBA ZAMÓWIEŃ']:
            html_chunk = html_chunk + '<td>'+i+'</td>'
        html_chunk = html_chunk+'</tr>'
        for i in most_ordered.index:
            html_chunk = html_chunk+'\n<tr><td>'+str(i)+'</td><td>'+str(most_ordered[i])+'</td></tr>'
        html_chunk = html_chunk+'\n</table></div>'
        file.write(html_chunk)

        html_chunk = '\n<div id=\"mst\"><table><tr class=\"head\">'
        for i in ['GRUPA', 'MAX', 'PAŃSTWA']:
            html_chunk = html_chunk + '<td>'+i+'</td>'
        html_chunk = html_chunk+'</tr>'
        for i in cntry_grps:
            html_chunk = html_chunk+'\n<tr><td>'+str(i[0])+'</td><td>'+str(i[1])+'</td><td>'
            for j in i[2]:
                html_chunk = html_chunk+j+', '
            html_chunk = html_chunk+'</td></tr>'
        html_chunk = html_chunk+'\n</table></div>'
        file.write(html_chunk)

        html_chunk = '\n<div id=\"mst\"><table><tr class=\"head\">'
        for i in ['STATUS', 'PLIK', 'MAX']:
            html_chunk = html_chunk + '<td>'+i+'</td>'
        html_chunk = html_chunk+'</tr>'
        for i in top_files:
            html_chunk = html_chunk+'\n<tr><td>'+str(i[0])+'</td><td>'+str(i[2])+'</td><td>'+str(i[1])+'</td></tr>'
        html_chunk = html_chunk+'\n</table></div>'
        file.write(html_chunk)


        html_chunk = '\n<div id=\"cns\"><table><tr class=\"head\"><td>LICZBA SPÓŁGŁOSEK</td></tr><tr><td>'+str(consonants_count)+'</td></tr></table></div>'
        file.write(html_chunk)

        html_chunk = '</body></html>'
        file.write(html_chunk)