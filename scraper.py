#scaper
import requests

def scrape():
    response = requests.get('https://projects.fivethirtyeight.com/2020-election-forecast/us_simulations.json')

    json_response = response.json()

    simulations = json_response[0]['simulations']

    results = { }
    for simulation in simulations:
        winner = simulation['winner']
        if winner not in results:
              results[winner] = 0
        results[winner] += 1


    print('Biden: {biden}%'.format(biden=results.get('Biden', 0)))
    print('Trump: {trump}%'.format(trump=results.get('Trump', 0)))
    print('Tie: {tie}%'.format(tie=results.get('no majority', 0)))


    return(results)