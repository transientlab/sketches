#include <vector>
#include <algorithm>
#include <iostream>

int times(const std::vector<std::pair<int, int>>& persons) {
    std::vector<int> events;
    
    // Store events in a sorted order: entry as positive, exit as negative
    for (const auto& p : persons) {
        events.push_back(p.first);
        events.push_back(-p.second);
    }
    
    std::sort(events.begin(), events.end(), [](int a, int b) {
        return std::abs(a) < std::abs(b); // Sort events by time, maintaining entry before exit
    });
    
    int count = 0; // Count of times the lights get switched on
    int roomCount = 0; // Number of people in the room
    
    for (const auto& e : events) {
        if (e >= 0) { // Entry event
            roomCount++;
            count++;
        } else { // Exit event
            roomCount--;
            if (roomCount == 0)
                count--;
        }
        std::cout << roomCount << std::endl;
    }
    
    return count;
}


int main (void) 
{
    std::vector<std::pair<int, int> > list1 = 
    {
        {1, 10},
        {2, 3},
        {4, 6},
        {7, 8}
    };
    std::cout << times(list1) << std::endl;

}