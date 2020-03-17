def two_sum(nums, target)
    return [] if nums.nil? or nums.empty? or target.nil?

    hashmap = {}

    nums.each_with_index do |number, i|
        complement = target - number

        i2 = hashmap.fetch(complement, nil)

        return [hashmap[complement], i] unless i2.nil?

        hashmap[number] = i
    end

    []
end
