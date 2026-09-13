def show_match_result(home_team, away_team, home_score, away_score):

    if home_score > away_score:
        print(f"{home_team} vant {home_score}-{away_score} over {away_team}!")
    elif home_score < away_score:
        print(f"{away_team} vant {away_score}-{home_score} over {home_team}!")
    elif home_score == away_score:
        print(f"{home_score}-{away_score} mellom {home_team} og {away_team} - uavgjort!")
    else:
        print("Noe gikk feil, prøv igjen.")

show_match_result("Liverpool", "Manchester United", 5, 0)
show_match_result("Bodø Glimt", "Lillestrøm", 1, 2)
show_match_result("PSG", "Real Madrid", 2, 2)