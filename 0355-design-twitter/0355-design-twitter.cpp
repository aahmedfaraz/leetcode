class Twitter {
    int timestamp = 0;

public:
    unordered_map <int, vector<pair<int, int>>> tweets; // userId: [pair = v{timestamp, tweetId}]
    unordered_map<int, unordered_set<int>> follows; // userId: s{followeeId}

    Twitter() {}

    void postTweet(int userId, int tweetId) {
        pair<int, int> tweet = {timestamp, tweetId};
        timestamp++;
        tweets[userId].push_back(tweet);
        if (tweets[userId].size() > 10) {
            tweets[userId].erase(tweets[userId].begin());
        }
    }

    vector<int> getNewsFeed(int userId) {
        vector<int> result;
        unordered_map<int, int> indices;

        for (int followee: follows[userId]) {
            indices[followee] = tweets[followee].size() - 1; // pointing to last element, if no elements pointing to -1
        }
        indices[userId] = tweets[userId].size() - 1;

        for (int i = 0; i < 10; i++) {
            int latPerId = -1;
            int latTweetId = -1;
            int latTime = INT_MIN;

            for (auto item: indices) {
                int personId = item.first;
                int tweetIdx = item.second;

                if (tweetIdx < 0)
                    continue;

                pair<int, int> tweet = tweets[personId][tweetIdx];
                int time = tweet.first;
                int tweetId = tweet.second;

                if (time > latTime) {
                    latPerId = personId;
                    latTweetId = tweetId;
                    latTime = time;
                }
            }

            if (latPerId == -1)
                break;

            indices[latPerId]--;
            
            result.push_back(latTweetId);
        }

        return result;
    }

    void follow(int followerId, int followeeId) {
        follows[followerId].insert(followeeId);
    }

    void unfollow(int followerId, int followeeId) {
        follows[followerId].erase(followeeId);
    }
};