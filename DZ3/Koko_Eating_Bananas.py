class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = left + (right - left) // 2

            hours = 0
            for p in piles:
                hours += (p - 1) // k + 1

            if hours <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res

# Пространство ответ так скажем отсортированно если сжирает за h со скоростью k то и с большей скоростью сожрёт и если не сжирает со скоростью k то и с меньшей не сожрёт из-за чего мы делаем бинарный поиск по пространсту ответов 
