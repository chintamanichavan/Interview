class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        # Sort the greed factor array and the size array
        g.sort()
        s.sort()

        child_i = 0  # Index for children
        cookie_j = 0  # Index for cookies
        content_children = 0  # Count of content children

        # Iterate over each child and each cookie
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                # If the cookie can satisfy the child's greed factor
                content_children += 1
                child_i += 1  # Move to the next child
            cookie_j += 1  # Move to the next cookie regardless

        return content_children
