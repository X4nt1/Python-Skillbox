import re
import requests
import json
from bs4 import BeautifulSoup

# 18.1
text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate
"""

four_letter_words = re.findall(r'\b\w{4}\b', text)
print(four_letter_words)



# 18.2
def find_car_and_taxi_numbers(text):
    private_car_pattern = re.compile(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b')
    taxi_pattern = re.compile(r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}\b')

    private_car_numbers = private_car_pattern.findall(text)
    taxi_numbers = taxi_pattern.findall(text)

    return private_car_numbers, taxi_numbers

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
private_cars, taxis = find_car_and_taxi_numbers(text)

print("Номера частных легковых автомобилей:", private_cars)
print("Номера такси:", taxis)



# 18.3
def get_millennium_falcon_info():
    url = "https://swapi.dev/api/starships/10/"
    response = requests.get(url)

    if response.status_code == 200:
        falcon_data = response.json()

        falcon_info = {
            "ship_name": falcon_data["name"],
            "max_atmosphering_speed": falcon_data["max_atmosphering_speed"],
            "starship_class": falcon_data["starship_class"],
            "pilots": []
        }

        for pilot_url in falcon_data["pilots"]:
            pilot_response = requests.get(pilot_url)
            if pilot_response.status_code == 200:
                pilot_data = pilot_response.json()
                planet_url = pilot_data["homeworld"]

                planet_response = requests.get(planet_url)
                if planet_response.status_code == 200:
                    planet_data = planet_response.json()

                    falcon_info["pilots"].append(planet_data)

        return falcon_data, falcon_info
    else:
        print("Ошибка при получении данных:", response.status_code)
        return None

def main():
    millennium_falcon_data, millennium_falcon_info = get_millennium_falcon_info()
    if millennium_falcon_info:
        print(json.dumps(millennium_falcon_info, indent=2, ensure_ascii=False))

        with open("millennium_falcon_info.json", "w", encoding="utf-8") as json_file:
            json.dump(millennium_falcon_info, json_file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()


# 18.4
def check_phone_numbers(phone_numbers):
    for number in phone_numbers:
        pattern = re.compile(r'^[89]\d{9}$')
        if pattern.match(number):
            print(f'{number}: всё в порядке')
        else:
            print(f'{number}: не подходит')

def main():
    phone_numbers_list = ['9999999999', '999999-999', '99999x9999']
    check_phone_numbers(phone_numbers_list)

if __name__ == '__main__':
    main()



# 18.5
def get_subheadings(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        subheadings = soup.find_all('h3')
        subheadings_text = [subheading.text.strip() for subheading in subheadings]
        return subheadings_text

    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    return []

def main():
    url = 'http://www.columbia.edu/~fdc/sample.html'
    subheadings_list = get_subheadings(url)
    print(subheadings_list)

if __name__ == '__main__':
    main()



# 18.6
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def find_differences(old_data, new_data, diff_list):
    result = {}
    for key in diff_list:
        if key in old_data and key in new_data:
            if old_data[key] != new_data[key]:
                result[key] = new_data[key]
    return result

def main():
    json_old_path = '18.6-old.json'
    json_new_path = '18.6-new.json'
    result_path = 'result.json'
    diff_list = ['services', 'staff', 'datetime']

    old_data = load_json(json_old_path)
    new_data = load_json(json_new_path)
    result = find_differences(old_data, new_data, diff_list)
    print(result)

    with open(result_path, 'w', encoding='utf-8') as result_file:
        json.dump(result, result_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()




