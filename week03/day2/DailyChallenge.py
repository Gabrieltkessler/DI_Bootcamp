import math

class Pagination:
    """
    Simulates a basic pagination system for slicing items into manageable pages.
    """
    def __init__(self, items=None, page_size=10):
        # Step 2: Initialize attributes
        self.items = items if items is not None else []
        self.page_size = int(page_size)
        self.current_idx = 0  # 0-based index internally
        
        # Calculate total pages (handle empty items list gracefully)
        if not self.items:
            self.total_pages = 1
        else:
            self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        """Step 3: Return the slice of items visible on the current page."""
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # CamelCase alias to support the bonus method chaining example syntax
    getVisibleItems = get_visible_items

    # Step 4: Navigation Methods
    def go_to_page(self, page_num):
        """
        Navigates to specified 1-based page number.
        Raises ValueError if out of range.
        """
        if not (1 <= page_num <= self.total_pages):
            raise ValueError(f"Page number {page_num} out of range (1 to {self.total_pages}).")
        
        self.current_idx = page_num - 1
        return self

    def first_page(self):
        """Navigates to the first page."""
        self.current_idx = 0
        return self

    def last_page(self):
        """Navigates to the last page."""
        self.current_idx = max(0, self.total_pages - 1)
        return self

    def next_page(self):
        """Moves one page forward if not on the last page."""
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        """Moves one page backward if not on the first page."""
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # CamelCase aliases for method chaining bonuses
    goToPage = go_to_page
    firstPage = first_page
    lastPage = last_page
    nextPage = next_page
    prevPage = previous_page
    previousPage = previous_page

    def __str__(self):
        """Step 5: Return string representation of current page items."""
        visible = self.get_visible_items()
        return "\n".join(str(item) for item in visible)


# ==============================================================================
# Step 6: Test Code Execution
# ==============================================================================
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print("Initial items (Page 1):", p.get_visible_items())  # ['a', 'b', 'c', 'd']

    p.next_page()
    print("After next_page() (Page 2):", p.get_visible_items())  # ['e', 'f', 'g', 'h']

    p.last_page()
    print("After last_page():", p.get_visible_items())  # ['y', 'z']

    # Testing Bonus Method Chaining
    p.first_page()
    chain_result = p.nextPage().nextPage().nextPage().getVisibleItems()
    print("Method Chaining Result:", chain_result)  # ['m', 'n', 'o', 'p']

    # Testing ValueError exceptions
    print("\nTesting Error Handling:")
    try:
        p.go_to_page(0)
    except ValueError as e:
        print("go_to_page(0) correctly raised ValueError:", e)

    try:
        p.go_to_page(10)
    except ValueError as e:
        print("go_to_page(10) correctly raised ValueError:", e)