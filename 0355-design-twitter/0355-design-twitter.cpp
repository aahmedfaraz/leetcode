class Twitter {
    int timestamp = 0;

public:
    unordered_map <int, vector<pair<int, int>>> tweets; // userId: [pair = v{timestamp, tweetId}]
    unordered_map<int, unordered_set<int>> follows; // userId: s{followeeId}

    Twitter() {}

    void postTweet(int userId, int tweetId) {
        tweets[userId].push_back({timestamp, tweetId});
        timestamp++;
        if (tweets[userId].size() > 10) {
            tweets[userId].erase(tweets[userId].begin());
        }
    }

    vector<int> getNewsFeed(int userId) {
        vector<int> result;
        priority_queue<tuple<int, int, int>> pq; // tuple = time, userId, index
        
        int tweetIdx = tweets[userId].size() - 1;
        if (tweetIdx >= 0) {
            auto [time, twId] = tweets[userId][tweetIdx];
            pq.push({time, userId, tweetIdx});
        }

        for (auto followeeId: follows[userId]) {
            tweetIdx = tweets[followeeId].size() - 1;
            if (tweetIdx >= 0) {
                auto [time, twId] = tweets[followeeId][tweetIdx];
                pq.push({time, followeeId, tweetIdx});
            }
        }

        if (pq.empty())
            return result;
        
        while (!pq.empty() && result.size() < 10) {
            auto [time, personId, index] = pq.top();
            auto [t, tweetId] = tweets[personId][index];
            pq.pop();

            result.push_back(tweetId);

            index--;
            if (index >= 0) {
                auto [newtime, newtweetId] = tweets[personId][index];
                pq.push({newtime, personId, index});
            }
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