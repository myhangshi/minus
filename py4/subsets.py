
def subsets(nums):
        # write your code here
        if len(nums) <= 0:
            return [[]]

        nums.sort()
        result = []
        run_list = []

        def gen_subsets(run_list, pos):
            result.append(list(run_list))
            print("getting recursive functions ", pos)
            print("run_list and result", run_list, result)

            for i in range(pos, len(nums)):
                run_list.append(nums[i])
                print("invoke ", i, pos, run_list) 
                gen_subsets(run_list, i + 1)

                k = run_list.pop()
                print("pop", k)

        gen_subsets(run_list, 0)

        return result

t1 = [1, 2]
result = subsets(t1) 
print(result) 

