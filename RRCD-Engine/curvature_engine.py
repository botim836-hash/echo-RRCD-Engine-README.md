"""
Curvature Engine Module

This module implements a Curvature Engine for the RRCD (Rapid Response Curvature Detection) system.
The engine analyzes and calculates curvature properties of geometric objects and paths.
"""

import math
from typing import List, Tuple, Optional


class CurvatureEngine:
    """
    A Curvature Engine that calculates and analyzes curvature properties.
    
    The engine supports:
    - Point-based curvature calculation
    - Path curvature analysis
    - Radius of curvature computation
    - Curvature smoothing and filtering
    """
    
    def __init__(self, precision: int = 6):
        """
        Initialize the Curvature Engine.
        
        Args:
            precision (int): Decimal precision for calculations (default: 6)
        """
        self.precision = precision
        self.version = "1.0.0"
        
    def calculate_curvature(self, points: List[Tuple[float, float]]) -> List[float]:
        """
        Calculate curvature at each point in a sequence.
        
        Args:
            points: List of (x, y) coordinate tuples
            
        Returns:
            List of curvature values at each point
            
        Raises:
            ValueError: If less than 3 points are provided
        """
        if len(points) < 3:
            raise ValueError("At least 3 points are required to calculate curvature")
        
        curvatures = []
        
        for i in range(1, len(points) - 1):
            p1, p2, p3 = points[i-1], points[i], points[i+1]
            curvature = self._compute_point_curvature(p1, p2, p3)
            curvatures.append(round(curvature, self.precision))
        
        return curvatures
    
    def _compute_point_curvature(self, p1: Tuple[float, float], 
                                  p2: Tuple[float, float], 
                                  p3: Tuple[float, float]) -> float:
        """
        Compute curvature at a point using three consecutive points.
        
        Uses the Menger curvature formula: k = 4*A / (a*b*c)
        where A is the area of the triangle and a, b, c are the side lengths.
        
        Args:
            p1, p2, p3: Three consecutive points (x, y)
            
        Returns:
            Curvature value at the middle point
        """
        # Calculate side lengths
        a = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        b = math.sqrt((p3[0] - p2[0])**2 + (p3[1] - p2[1])**2)
        c = math.sqrt((p3[0] - p1[0])**2 + (p3[1] - p1[1])**2)
        
        # Avoid division by zero
        if a == 0 or b == 0 or c == 0:
            return 0.0
        
        # Calculate area using cross product
        area = abs((p2[0] - p1[0]) * (p3[1] - p1[1]) - 
                   (p3[0] - p1[0]) * (p2[1] - p1[1])) / 2.0
        
        # Menger curvature
        curvature = (4 * area) / (a * b * c)
        
        return curvature
    
    def radius_of_curvature(self, curvature: float) -> Optional[float]:
        """
        Calculate the radius of curvature from a curvature value.
        
        Args:
            curvature: Curvature value
            
        Returns:
            Radius of curvature, or None if curvature is zero
        """
        if curvature == 0:
            return None
        
        return round(1.0 / abs(curvature), self.precision)
    
    def max_curvature(self, points: List[Tuple[float, float]]) -> Tuple[float, int]:
        """
        Find the maximum curvature in a path.
        
        Args:
            points: List of (x, y) coordinate tuples
            
        Returns:
            Tuple of (max_curvature_value, index_in_path)
            
        Raises:
            ValueError: If less than 3 points are provided
        """
        curvatures = self.calculate_curvature(points)
        max_curv = max(curvatures)
        max_idx = curvatures.index(max_curv) + 1  # +1 because first point has no curvature
        
        return (max_curv, max_idx)
    
    def average_curvature(self, points: List[Tuple[float, float]]) -> float:
        """
        Calculate the average curvature along a path.
        
        Args:
            points: List of (x, y) coordinate tuples
            
        Returns:
            Average curvature value
            
        Raises:
            ValueError: If less than 3 points are provided
        """
        curvatures = self.calculate_curvature(points)
        return round(sum(curvatures) / len(curvatures), self.precision)
    
    def is_straight(self, points: List[Tuple[float, float]], 
                    threshold: float = 0.01) -> bool:
        """
        Determine if a path is approximately straight.
        
        Args:
            points: List of (x, y) coordinate tuples
            threshold: Maximum curvature to consider straight
            
        Returns:
            True if path is approximately straight, False otherwise
        """
        avg_curv = self.average_curvature(points)
        return abs(avg_curv) < threshold
    
    def get_info(self) -> dict:
        """
        Get information about the Curvature Engine.
        
        Returns:
            Dictionary containing engine information
        """
        return {
            "name": "Curvature Engine",
            "version": self.version,
            "precision": self.precision,
            "capabilities": [
                "Point curvature calculation",
                "Path curvature analysis",
                "Radius of curvature computation",
                "Maximum curvature detection",
                "Average curvature calculation",
                "Straightness detection"
            ]
        }


def main():
    """
    Demonstration of the Curvature Engine functionality.
    """
    print("=" * 60)
    print("RRCD Curvature Engine Demo")
    print("=" * 60)
    
    # Initialize the engine
    engine = CurvatureEngine(precision=4)
    
    # Display engine info
    info = engine.get_info()
    print(f"\nEngine: {info['name']} v{info['version']}")
    print(f"Precision: {info['precision']} decimal places")
    print("\nCapabilities:")
    for capability in info['capabilities']:
        print(f"  - {capability}")
    
    # Example 1: Circular arc
    print("\n" + "-" * 60)
    print("Example 1: Circular Arc")
    print("-" * 60)
    circle_points = [
        (0, 0), (1, 1), (2, 1.414), (3, 1), (4, 0)
    ]
    print(f"Points: {circle_points}")
    curvatures = engine.calculate_curvature(circle_points)
    print(f"Curvatures: {curvatures}")
    
    max_curv, max_idx = engine.max_curvature(circle_points)
    print(f"Maximum curvature: {max_curv} at index {max_idx}")
    
    radius = engine.radius_of_curvature(max_curv)
    print(f"Radius of curvature: {radius}")
    
    # Example 2: Straight line
    print("\n" + "-" * 60)
    print("Example 2: Straight Line")
    print("-" * 60)
    line_points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    print(f"Points: {line_points}")
    curvatures = engine.calculate_curvature(line_points)
    print(f"Curvatures: {curvatures}")
    
    avg_curv = engine.average_curvature(line_points)
    print(f"Average curvature: {avg_curv}")
    print(f"Is straight: {engine.is_straight(line_points)}")
    
    # Example 3: Sharp turn
    print("\n" + "-" * 60)
    print("Example 3: Sharp Turn")
    print("-" * 60)
    turn_points = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    print(f"Points: {turn_points}")
    curvatures = engine.calculate_curvature(turn_points)
    print(f"Curvatures: {curvatures}")
    
    max_curv, max_idx = engine.max_curvature(turn_points)
    print(f"Maximum curvature: {max_curv} at index {max_idx}")
    print(f"Is straight: {engine.is_straight(turn_points)}")
    
    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
