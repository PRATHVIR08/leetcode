class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in asteroids:
            if i>0:
                st.append(i)
            else:
                while st and st[-1]>0 and st[-1]<abs(i):
                    st.pop()
                if st and st[-1]==abs(i):
                    st.pop()
                    continue
                elif st and st[-1]>abs(i):
                    continue
                st.append(i)
        return st