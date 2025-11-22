# Curvature Engine Documentation

## Overview

The **Curvature Engine** is a core component of the RRCD (Rapid Response Curvature Detection) system. It provides advanced algorithms for calculating and analyzing the curvature of geometric paths and objects.

## Features

- **Point-based Curvature Calculation**: Calculate curvature at specific points along a path
- **Path Curvature Analysis**: Analyze the curvature properties of entire paths
- **Radius of Curvature Computation**: Convert curvature values to radius of curvature
- **Maximum Curvature Detection**: Identify the point of maximum curvature in a path
- **Average Curvature Calculation**: Compute the average curvature along a path
- **Straightness Detection**: Determine if a path is approximately straight

## Installation

The Curvature Engine is part of the RRCD-Engine package. To use it, simply import:

```python
from RRCD_Engine import CurvatureEngine
```

## Quick Start

### Basic Usage

```python
from RRCD_Engine.curvature_engine import CurvatureEngine

# Initialize the engine
engine = CurvatureEngine(precision=4)

# Define a path as a list of (x, y) points
path = [(0, 0), (1, 1), (2, 1.414), (3, 1), (4, 0)]

# Calculate curvature at each point
curvatures = engine.calculate_curvature(path)
print(f"Curvatures: {curvatures}")

# Find maximum curvature
max_curv, max_idx = engine.max_curvature(path)
print(f"Max curvature: {max_curv} at index {max_idx}")

# Calculate radius of curvature
radius = engine.radius_of_curvature(max_curv)
print(f"Radius: {radius}")
```

### Advanced Usage

```python
# Check if a path is straight
line_points = [(0, 0), (1, 1), (2, 2), (3, 3)]
is_straight = engine.is_straight(line_points, threshold=0.01)
print(f"Path is straight: {is_straight}")

# Calculate average curvature
avg_curvature = engine.average_curvature(path)
print(f"Average curvature: {avg_curvature}")

# Get engine information
info = engine.get_info()
print(f"Engine version: {info['version']}")
```

## API Reference

### CurvatureEngine Class

#### Constructor

```python
CurvatureEngine(precision=6)
```

**Parameters:**
- `precision` (int): Decimal precision for calculations (default: 6)

#### Methods

##### calculate_curvature(points)

Calculate curvature at each point in a sequence.

**Parameters:**
- `points` (List[Tuple[float, float]]): List of (x, y) coordinate tuples

**Returns:**
- `List[float]`: List of curvature values

**Raises:**
- `ValueError`: If less than 3 points are provided

##### radius_of_curvature(curvature)

Calculate the radius of curvature from a curvature value.

**Parameters:**
- `curvature` (float): Curvature value

**Returns:**
- `Optional[float]`: Radius of curvature, or None if curvature is zero

##### max_curvature(points)

Find the maximum curvature in a path.

**Parameters:**
- `points` (List[Tuple[float, float]]): List of (x, y) coordinate tuples

**Returns:**
- `Tuple[float, int]`: Tuple of (max_curvature_value, index_in_path)

##### average_curvature(points)

Calculate the average curvature along a path.

**Parameters:**
- `points` (List[Tuple[float, float]]): List of (x, y) coordinate tuples

**Returns:**
- `float`: Average curvature value

##### is_straight(points, threshold=0.01)

Determine if a path is approximately straight.

**Parameters:**
- `points` (List[Tuple[float, float]]): List of (x, y) coordinate tuples
- `threshold` (float): Maximum curvature to consider straight (default: 0.01)

**Returns:**
- `bool`: True if path is approximately straight, False otherwise

##### get_info()

Get information about the Curvature Engine.

**Returns:**
- `dict`: Dictionary containing engine information

## Mathematical Background

The Curvature Engine uses the **Menger curvature formula** to calculate curvature at a point:

```
k = 4*A / (a*b*c)
```

Where:
- `k` is the curvature
- `A` is the area of the triangle formed by three consecutive points
- `a`, `b`, `c` are the side lengths of the triangle

The radius of curvature `R` is calculated as:

```
R = 1 / |k|
```

## Examples

### Example 1: Circular Arc

```python
engine = CurvatureEngine()
circle_points = [(0, 0), (1, 1), (2, 1.414), (3, 1), (4, 0)]
curvatures = engine.calculate_curvature(circle_points)
# Output: [0.353553, 0.5, 0.353553]
```

### Example 2: Straight Line

```python
engine = CurvatureEngine()
line_points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
curvatures = engine.calculate_curvature(line_points)
# Output: [0.0, 0.0, 0.0]
print(engine.is_straight(line_points))  # True
```

### Example 3: Sharp Turn

```python
engine = CurvatureEngine()
turn_points = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
max_curv, max_idx = engine.max_curvature(turn_points)
print(f"Sharpest turn at index {max_idx} with curvature {max_curv}")
```

## Running the Demo

To see the Curvature Engine in action, run the included demo:

```bash
python RRCD-Engine/curvature_engine.py
```

This will demonstrate:
- Circular arc curvature calculation
- Straight line detection
- Sharp turn analysis

## Performance Considerations

- The engine is optimized for paths with hundreds to thousands of points
- Precision can be adjusted to balance accuracy vs. performance
- All calculations use standard Python math libraries for portability

## Error Handling

The Curvature Engine handles common edge cases:
- Returns 0.0 for zero-length segments
- Returns None for radius of curvature when curvature is zero
- Raises `ValueError` for insufficient points (< 3)

## Version History

- **v1.0.0**: Initial release
  - Core curvature calculation
  - Path analysis features
  - Comprehensive documentation

## License

This is part of the RRCD-Engine project.

## Support

For questions or issues, please refer to the main RRCD-Engine README.
