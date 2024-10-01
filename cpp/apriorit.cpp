
// c++ 11
#include <iostream>
#include <vector>
#include <algorithm>






int main(void) 
{

    // dummy data
    std::vector<std::pair<int, int> > list1 = 
    {
        {30, 9},
        {10, 7},
        {20, 6}
    };


    std::cout << list1.size() << std::endl;

    std::sort(list1.begin(), list1.end(), [](auto &left, auto &right) {
    return left.first < right.first;
    });

    int double_size = list1.size() * 2;
    int ee_array[double_size][2];

    int k = 0;
    std::vector<std::pair<int, int> > list2;
    for (const auto& [first, second] : list1)
    {
        ee_array[k][0] = first;
        ee_array[k][1] = 1;
        ee_array[k+1][0] = second;
        ee_array[k+1][1] = 0;
        k+=2;
    }

    

    std::sort(std::begin(ee_array), std::end(ee_array), comparator);
    for (int i = 0; i < double_size; i++)
    {
        std::cout << ee_array[i][0] << " " << ee_array[i][1] << std::endl;
    }



    return 0; 
}


