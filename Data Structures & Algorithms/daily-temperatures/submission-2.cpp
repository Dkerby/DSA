class Solution {
   public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> result(temperatures.size(), 0);
        stack<int> st;

        for (int i = 0; i < temperatures.size(); i++) {
            while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
                int diff = i - st.top();
                result[st.top()] = diff;
                st.pop();
            }
            st.push(i);
        }

        return result;
    }
};
