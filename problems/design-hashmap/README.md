
# Leetcode: Design HashMap     :BLOG:Basic:

---

Design HashMap  

---

Similar Problems:  

-   [Leetcode: Design HashSet](https://code.dennyzhang.com/design-hashset)
-   Tag: [#oodesign](https://code.dennyzhang.com/tag/oodesign)

---

Design a HashMap without using any built-in hash table libraries.  

To be specific, your design should include these functions:  

-   put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
-   get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
-   remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:  

    MyHashMap hashMap = new MyHashMap();
    hashMap.put(1, 1);          
    hashMap.put(2, 2);         
    hashMap.get(1);            // returns 1
    hashMap.get(3);            // returns -1 (not found)
    hashMap.put(2, 1);          // update the existing value
    hashMap.get(2);            // returns 1 
    hashMap.remove(2);          // remove the mapping for 2
    hashMap.get(2);            // returns -1 (not found) 

Note:  

-   All keys and values will be in the range of [0, 1000000].
-   The number of operations will be in the range of [1, 10000].
-   Please do not use the built-in HashMap library.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/design-hashmap)  

Credits To: [leetcode.com](https://leetcode.com/problems/design-hashmap/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/design-hashmap
    // Basic Ideas: array
    // Complexity: Time O(1), Space O(1). 1,000,000 items
    type MyHashMap struct {
        m []int
    }
    
    
    /** Initialize your data structure here. */
    func Constructor() MyHashMap {
        res := MyHashMap{}
        res.m = make([]int, 1000001)
        for i, _ := range res.m {
    	res.m[i] = -1
        }
        return res
    }
    
    
    /** value will always be non-negative. */
    func (this *MyHashMap) Put(key int, value int)  {
        this.m[key] = value
    }
    
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    func (this *MyHashMap) Get(key int) int {
        return this.m[key]
    }
    
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    func (this *MyHashMap) Remove(key int)  {
        this.m[key] = -1
    }
    
    
    /**
     * Your MyHashMap object will be instantiated and called as such:
     * obj := Constructor();
     * obj.Put(key,value);
     * param_2 := obj.Get(key);
     * obj.Remove(key);
     */
