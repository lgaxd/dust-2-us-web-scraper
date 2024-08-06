import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_recent_results():
    url = 'https://www.dust2.us/results'
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    

    results_section = soup.find('div', {'class': 'results-page-content'})
    if not results_section:
        print("No results section found")
        return None
    
    matches = results_section.find_all('div', class_='match')
    if not matches:
        print("No matches found")
        return None
    
    recent_results = []
    today = datetime.now()

    for match in matches:

        timestamp = match.find('span', {'data-controller': 'date-time-controller'}).get('data-date')
        match_date = datetime.fromtimestamp(int(timestamp) / 1000)
        
        teams = match.find_all('div', class_='match-team')
        if len(teams) < 2:
            continue
        
        team1 = teams[0].find('div', class_='match-team-name').get_text(strip=True)
        team2 = teams[1].find('div', class_='match-team-name').get_text(strip=True)
        
        match_results = match.find('div', class_='match-results')
        score1 = match_results.find('a', class_='match-team match-result team-1').get_text(strip=True)
        score2 = match_results.find('a', class_='match-team match-result team-2').get_text(strip=True)
        
        recent_results.append({
            'date': match_date.strftime('%Y-%m-%d %H:%M'),
            'team1': team1,
            'team2': team2,
            'score1': score1,
            'score2': score2
        })
    
    return recent_results

if __name__ == '__main__':
    recent_results = get_recent_results()
    if recent_results:
        for match in recent_results:
            print(f"{match['date']}: {match['team1']} {match['score1']} - {match['team2']} {match['score2']}")