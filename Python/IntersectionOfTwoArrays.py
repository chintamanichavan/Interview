
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        result = []

        # Assuming we have a function that reads chunks of nums2 from disk
        for chunk in read_chunks_from_disk(nums2):
            for num in chunk:
                if counts[num] > 0:
                    result.append(num)
                    counts[num] -= 1

        return result

# Function to simulate reading chunks from disk (not actual implementation)
def read_chunks_from_disk(nums2):
    chunk_size = 100  # Example chunk size
    for i in range(0, len(nums2), chunk_size):
        yield nums2[i:i + chunk_size]
