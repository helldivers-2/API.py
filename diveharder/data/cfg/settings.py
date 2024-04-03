import os
from dotenv import load_dotenv

if os.path.isfile("./.env"):
    load_dotenv()

news_feed_max_entries = "?maxEntries=1024"
steam_news_query_params = "?appid=553850&feeds=steam_community_announcements"

api = {
    "BASE_URL": os.environ["BASE_URL"],
    "TIME_DELAY": os.environ["TIME_DELAY"],
    "TIMEOUT": os.environ["TIMEOUT"],
    "STATUS_API_URL": os.environ["STATUS_API_URL"],
    "WARINFO_API_URL": os.environ["WARINFO_API_URL"],
    "NEWS_TICKER_API_URL": os.environ["NEWS_TICKER_API_URL"],
    "NEWS_FEED_API_URL": os.environ["NEWS_FEED_API_URL"] + news_feed_max_entries,
    "TIMESINCESTART_API_URL": os.environ["TIMESINCESTART_API_URL"],
    "WARID_API_URL": os.environ["WARID_API_URL"],
    "GALACTICE_WAR_EFFECTS_API_URL": os.environ["GALACTICE_WAR_EFFECTS_API_URL"],
    "LEVELSPEC_API_URL": os.environ["LEVELSPEC_API_URL"],
    "ITEMS_API_URL": os.environ["ITEMS_API_URL"],
    "MISSION_REWARD_API_URL": os.environ["MISSION_REWARD_API_URL"],
    "HOTF_LEADERBOARD_API_URL": os.environ["HOTF_LEADERBOARD_API_URL"],
    "PLANET_STATS_API_URL": os.environ["PLANET_STATS_API_URL"],
    "MAJOR_ORDER_API_URL": os.environ["MAJOR_ORDER_API_URL"],
    "STOREFRONT_API_URL": os.environ["STOREFRONT_API_URL"],
    "STOREFRONT_ROTATION_API_URL": os.environ["STOREFRONT_ROTATION_API_URL"],
    "SEASONPASS_API_URL": os.environ["SEASONPASS_API_URL"],
    "SCORE_CALC_PARAMS_API_URL": os.environ["SCORE_CALC_PARAMS_API_URL"],
    "MINIGAME_LEADERBOARD_API_URL": os.environ["MINIGAME_LEADERBOARD_API_URL"],
    "HOTF_CLAN_LEADBOARD_API_URL": os.environ["HOTF_CLAN_LEADBOARD_API_URL"],
    "ELECTION_CANDIDATES_API_URL": os.environ["ELECTION_CANDIDATES_API_URL"],
    "ELECTION_TERMS_API_URL": os.environ["ELECTION_TERMS_API_URL"],
    "ELECTION_POLICIES_API_URL": os.environ["ELECTION_POLICIES_API_URL"],
    "STEAM_NEWS_API_URL": os.environ["STEAM_NEWS_API_URL"] + steam_news_query_params,
}
