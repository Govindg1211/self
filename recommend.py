def get_user_preferences():
    print("Welcome to the Leisure Time Recommendation Program!")
    print("Please answer the following questions to help us suggest activities for you.")

    # Ask for user preferences
    mood = input("How do you feel today? (happy/sad/energetic/relaxed): ").strip().lower()
    indoors_outdoors = input("Do you prefer indoor or outdoor activities? (indoor/outdoor): ").strip().lower()
    social_preference = input("Do you want to do something alone or with others? (alone/with others): ").strip().lower()

    return mood, indoors_outdoors, social_preference

def recommend_activity(mood, indoors_outdoors, social_preference):
    recommendations = []

    # Recommend based on mood
    if mood == "happy":
        recommendations.append("You might enjoy going for a hike or having a picnic!")
    elif mood == "sad":
        recommendations.append("How about watching a comforting movie or reading a good book?")
    elif mood == "energetic":
        recommendations.append("Consider going for a run or trying out a new sport!")
    elif mood == "relaxed":
        recommendations.append("A nice yoga session or meditation could be perfect for you.")

    # Recommend based on indoor/outdoor preference
    if indoors_outdoors == "indoor":
        recommendations.append("You could try cooking a new recipe or starting a craft project.")
    elif indoors_outdoors == "outdoor":
        recommendations.append("Why not take a walk in the park or explore your local area?")

    # Recommend based on social preference
    if social_preference == "alone":
        recommendations.append("You might enjoy some solo time with a puzzle or journaling.")
    elif social_preference == "with others":
        recommendations.append("How about organizing a game night with friends or going out for coffee?")

    return recommendations

def display_recommendations(recommendations):
    print("\nHere are some activities you might enjoy:")
    for activity in recommendations:
        print(f"- {activity}")

def main():
    mood, indoors_outdoors, social_preference = get_user_preferences()
    recommendations = recommend_activity(mood, indoors_outdoors, social_preference)
    display_recommendations(recommendations)

if __name__ == "__main__":
    main()