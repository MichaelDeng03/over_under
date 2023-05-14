from nba_api.stats.endpoints import playercareerstats

# Retry Wrapper 
def retry(func, retries=3):
    '''
    This will prevent the HTTP Timeouts from stopping the script's run during API calls.
    '''
    def retry_wrapper(*args, **kwargs):
        attempts = 0
        while attempts < retries:
            try:
                return func(*args, **kwargs)
            except requests.exceptions.RequestException as e:
                print(e)
                time.sleep(30)
                attempts += 1

    return retry_wrapper


class game():
    def __init__(self, team1, team2, date):
        self.team1 = team1
        self.team2 = team2
        self.date = date


def predict(player, season, game):