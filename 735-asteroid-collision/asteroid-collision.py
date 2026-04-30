from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        
        for i in asteroids:
            # Handle collisions only when stack top is moving right and current is moving left
            while st and i < 0 and st[-1] > 0:
                if st[-1] < -i:
                    st.pop()  # stack asteroid explodes
                    continue
                elif st[-1] == -i:
                    st.pop()  # both explode
                break
            else:
                # This else belongs to while (runs if no break)
                st.append(i)
        
        return st