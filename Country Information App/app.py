import streamlit as st
import requests

def get_country_info(country_name):
    url = f"https://restcountries.com/v3/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        country_data = data[0]
        name = country_data["name"]["common"]
        capital = country_data["capital"][0]
        population = country_data["population"]
        area = country_data["area"]
        currency = country_data["currencies"]
        region = country_data["region"]
        return name, capital, population, area, currency, region
    else:
        return None
    
def main():
    st.title("Country Information App")

    country_name = st.text_input("Enter any country name:")

    if country_name:
        country_info = get_country_info(country_name)

        if country_info:
            name, capital, population, area, currency, region = country_info

            st.subheader("Country Information")
            st.write(f"Name: {name}")
            st.write(f"Capital: {capital}")
            st.write(f"Population: {population}")
            st.write(f"Area: {area}")
            st.write(f"Currency: {currency}")
            st.write(f"Region: {region}")
        else:
            st.error("Error: There is no existing data with the country name you input.")

if __name__ == "__main__":
    main()