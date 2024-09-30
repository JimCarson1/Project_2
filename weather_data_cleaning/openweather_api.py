import pandas as pd
import os
from dotenv import load_dotenv
import requests
import json
import time

load_dotenv('../keys.env')
api_key = os.getenv('WEATHER_KEY')

state_coordinates_min = {
    "Alabama": [(33.037792, -86.649186),
                ],
    "Alaska": [(63.229832, -157.899314)
               ],
    "Arizona": [(34.848374, -112.391468),
                ],
    "Arkansas": [(34.523767, -92.002740),
                 ],
    "California": [(34.792912, -117.455354),
                   (38.408393, -121.647267),
                   ],
    "Colorado": [(39.123936, -104.160885),
                 ],
    "Connecticut": [(41.749556, -72.948335),
                    ],
    "Delaware": [(38.920482, -75.526446),
                 ],
    "Florida": [(28.617751, -81.860728),
                ],
    "Georgia": [(33.098469, -83.699618),
                ],
    "Hawaii": [(19.512224, -155.085302),
               ],
    "Idaho": [(43.223527, -114.159762)
              ],
    "Illinois": [(40.498668, -89.279647),
                 ],
    "Indiana": [(40.322493, -86.259465),
                ],
    "Iowa": [(42.199769, -93.883877),
             ],
    "Kansas": [(38.730367, -98.688700),
               ],
    "Kentucky": [(37.861550, -85.168703),
                 ],
    "Louisiana": [(31.656455, -92.516194),
                  ],
    "Maine": [(45.204518, -69.136217),
              ],
    "Maryland": [(39.484643, -77.138621),
                 ],
    "Massachusetts": [(42.355751, -72.168424),
                      ],
    "Michigan": [(43.475072, -85.080875),
                 ],
    "Minnesota": [(45.988408, -94.777892),
                  ],
    "Mississippi": [(32.858701, -89.734574),
                    ],
    "Missouri": [(38.717234, -92.906736),
                 ],
    "Montana": [(47.107494, -108.453052),
                ],
    "Nebraska": [(41.709472, -99.578038),
                 ],
    "Nevada": [(39.623143, -117.581340),
               ],
    "New Hampshire": [(43.244486, -72.007446),
                      ],
    "New Jersey": [(39.740591, -74.645410),
                   ],
    "New Mexico": [(34.753133, -105.979112),
                   ],
    "New York": [(43.313959, -75.524170),
                 ],
    "North Carolina": [(35.852080, -79.334009),
                       ],
    "North Dakota": [(47.247497, -100.356443),
                     ],
    "Ohio": [(40.228719, -82.647549),
             ],
    "Oklahoma": [(35.843044, -97.745194),
                 ],
    "Oregon": [(43.666071, -119.978052),
               ],
    "Pennsylvania": [(41.055700, -78.917754),
                     ],
    "Rhode Island": [(41.782339, -71.565770),
                     ],
    "South Carolina": [(34.289708, -81.172899),
                       ],
    "South Dakota": [(44.292544, -100.726534),
                     ],
    "Tennessee": [(35.745511, -86.771622),
                  ],
    "Texas": [(29.997786, -97.028602),
              (32.832735, -100.783790),
              ],
    "Utah": [(39.475284, -112.568513),
             ],
    "Vermont": [(44.064045, -72.652140),
                ],
    "Virginia": [(37.662589, -78.407545),
                 ],
    "Washington": [(46.900238, -118.882080),
                   ],
    "West Virginia": [(38.798299, -81.144824),
                      ],
    "Wisconsin": [(44.920824, -90.294052),
                  ],
    "Wyoming": [(42.845280, -107.888595),
                ]
}

# Initialize state dictionary to store responses
state_dict = {state: [] for state in state_coordinates_min.keys()}

# Define the range of years
start_year = 1980
end_year = 2025

# Generate the list of dates
dates_list = []

for year in range(start_year, end_year):
    quarterly_dates = pd.date_range(start=f'{year}-01-16', periods=24, freq='15D')  # 24 dates per year
    dates_list.extend(quarterly_dates.strftime('%Y-%m-%d').tolist())

drop_dates = [
    '2024-07-14', '2024-07-29', '2024-08-13', '2024-08-28',
    '2024-09-12', '2024-09-27', '2024-10-12', '2024-10-27',
    '2024-11-11', '2024-11-26', '2024-12-11', '2024-12-26'
]

filtered_dates = [date for date in dates_list if date not in drop_dates]

# Directory to store state data files
output_dir = 'state_data'

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Missing response stores lists of missings responses from api
missing_response = []

# Loop over each state and grab corresponding coordinate
for state, coord_list in state_coordinates_min.items():
    state_data = []
    for coord in coord_list:
        lat, lon = coord
        for date in filtered_dates: # Loops through years 1980 - 2024 and every 15 days

            print(f"State: {state} Lat: {lat}, Lon: {lon} Date: {date}")
            try:
                response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&date={date}&appid={api_key}")

                if response.status_code == 200:
                    data = response.json()

                    state_data.append({date: data})
                    print("SUCCESSFUL")

                else:
                    print(f"Failed to get data for {state} on {date}: {response.status_code}")
                    missing_response.append({"State": state,
                                             "Coordinate": coord,
                                             "Date": date,
                                             "Status Code": response.status_code})

            except Exception as e:
                print(f"An error occurred: {e}")
                missing_response.append({"State": state,
                                    "Coordinate": coord,
                                    "Date": date,
                                    "Error": str(e)
                                    })

    # After collecting data for the current state, write it to a file
    state_filename = f"{state.replace(' ', '_')}.json"
    state_filepath = os.path.join(output_dir, state_filename)

    # Write the state_data to a JSON file
    with open(state_filepath, 'w') as f:
        json.dump(state_data, f)

    print(f"Data for {state} written to {state_filepath}")

    # Write missing responses to a JSON file
    if missing_response:
        missing_responses_filepath = os.path.join(output_dir, 'missing_responses.json')
        with open(missing_responses_filepath, 'w') as f:
            json.dump(missing_response, f)
        print(f"Missing responses written to {missing_responses_filepath}")

    # Sleep for 60 seconds after completion of collecting a states data
    print(f"{state} Success sleeping for 10 seconds.")
    time.sleep(10)