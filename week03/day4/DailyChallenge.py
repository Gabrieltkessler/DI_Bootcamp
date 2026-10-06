import math


class Circle:
    """
    Represents a circle defined by either radius or diameter.
    
    Demonstrates property decorators, string representations, arithmetic dunder
    methods, and comparison operators for list sorting.
    """

    def __init__(self, radius: float = 0.0):
        self.radius = float(radius)

    # -------------------------------------------------------------------------
    # Radius & Diameter Property Decorators
    # -------------------------------------------------------------------------
    @property
    def radius(self) -> float:
        """Get the circle's radius."""
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """Set the circle's radius (must be non-negative)."""
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = float(value)

    @property
    def diameter(self) -> float:
        """Get the circle's diameter."""
        return self._radius * 2

    @diameter.setter
    def diameter(self, value: float):
        """Set the circle's radius via its diameter."""
        if value < 0:
            raise ValueError("Diameter cannot be negative.")
        self._radius = value / 2.0

    @classmethod
    def from_diameter(cls, diameter: float):
        """Alternate constructor to instantiate a Circle directly using diameter."""
        return cls(radius=diameter / 2.0)

    # -------------------------------------------------------------------------
    # Computed Area Property
    # -------------------------------------------------------------------------
    @property
    def area(self) -> float:
        """Compute and return the area of the circle (pi * r^2)."""
        return math.pi * (self._radius ** 2)

    # -------------------------------------------------------------------------
    # String Representation Dunder Methods
    # -------------------------------------------------------------------------
    def __str__(self) -> str:
        return f"Circle(radius={self.radius:.2f})"

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"

    # -------------------------------------------------------------------------
    # Arithmetic Dunder Methods
    # -------------------------------------------------------------------------
    def __add__(self, other):
        """Add two circles to return a new Circle whose radius is the sum of both radii."""
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        elif isinstance(other, (int, float)):
            return Circle(self.radius + float(other))
        return NotImplemented

    # -------------------------------------------------------------------------
    # Comparison Dunder Methods (Enables sorting lists of circles)
    # -------------------------------------------------------------------------
    def __eq__(self, other) -> bool:
        if isinstance(other, Circle):
            return math.isclose(self.radius, other.radius)
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented


# ==============================================================================
# Optional Bonus: Turtle Drawing Visualization
# ==============================================================================
def draw_sorted_circles(circles: list[Circle]):
    """Draws a list of sorted circles using Python's standard turtle module."""
    try:
        import turtle
    except ImportError:
        print("Turtle module unavailable in this environment.")
        return

    screen = turtle.Screen()
    screen.title("Sorted Circles Visualization")

    t = turtle.Turtle()
    t.speed(3)

    # Scale factor for display
    scale = 10

    for c in circles:
        t.penup()
        t.goto(0, -c.radius * scale)  # Center circle on origin
        t.pendown()
        t.circle(c.radius * scale)

    turtle.done()


# ==============================================================================
# Test Runner
# ==============================================================================
if __name__ == "__main__":
    print("--- 1. Instantiation & Property Decorator Test ---")
    c1 = Circle(5)
    print(f"c1 radius: {c1.radius}")      # 5.0
    print(f"c1 diameter: {c1.diameter}")  # 10.0
    print(f"c1 area: {c1.area:.4f}")      # 78.5398

    # Set diameter directly via setter decorator
    c1.diameter = 20
    print(f"\nAfter setting c1.diameter = 20:")
    print(f"c1 radius: {c1.radius}")      # 10.0
    print(f"c1 diameter: {c1.diameter}")  # 20.0

    print("\n--- 2. String Representations (__str__ / __repr__) ---")
    c2 = Circle(3)
    print("str(c2):", str(c2))            # Circle(radius=3.00)
    print("repr(c2):", repr(c2))          # Circle(radius=3)

    print("\n--- 3. Addition (__add__) ---")
    c3 = c1 + c2
    print(f"{c1} + {c2} = {c3}")           # Circle(radius=13.00)

    print("\n--- 4. Comparisons (__gt__ / __eq__) ---")
    c4 = Circle(10)
    print(f"Is c1 == c4? {c1 == c4}")       # True
    print(f"Is c3 > c2? {c3 > c2}")         # True
    print(f"Is c2 > c3? {c2 > c3}")         # False

    print("\n--- 5. Sorting Multiple Circles (__lt__) ---")
    circles_list = [Circle(12), Circle(2), Circle(8), Circle(5), Circle(1)]
    print("Unsorted:", circles_list)

    circles_list.sort()
    print("Sorted:  ", circles_list)

    # Uncomment below to launch Turtle graphics locally:
    # draw_sorted_circles(circles_list)