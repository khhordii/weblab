import urllib.request
import urllib.parse
import json

def main():
    expression = input("Введіть алгебраїчний вираз для спрощення (наприклад, (x-1)*x): ")

    encoded_expression = urllib.parse.quote(expression)

    url = f"https://newton.vercel.app/api/v2/simplify/{encoded_expression}"

    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = response.read().decode('utf-8')

                json_data = json.loads(data)

                print("\n--- Результат API ---")
                print(f"Операція: {json_data.get('operation')}")
                print(f"Оригінальний вираз: {json_data.get('expression')}")
                print(f"Спрощений вираз: {json_data.get('result')}")
            else:
                print(f"Помилка: отримано статус код {response.status}")

    except urllib.error.URLError as e:
        print(f"Помилка з'єднання: {e.reason}")
    except json.JSONDecodeError:
        print("Помилка обробки JSON відповіді.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()