class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
  
        vector<int> freq(26, 0);
        

        for (char task : tasks) {
            freq[task - 'A']++;
        }
        

        int maxfreq = 0;
        int ind = -1;
        for (int i = 0; i < 26; i++) {
            if (maxfreq < freq[i]) {
                maxfreq = freq[i];
                ind = i;
            }
        }


        int idle_time = (maxfreq - 1) * n;
        

        for (int i = 0; i < 26; i++) {
            if (i != ind) {
                idle_time -= min(maxfreq - 1, freq[i]);
            }
        }

        return tasks.size() + max(idle_time, 0);
    }
};