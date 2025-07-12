# Copilot Instructions for Algorithms Repository

## Project Overview
This is a Python-based algorithms and data structures repository organized for interview preparation and coding practice. It contains implementations of classic algorithms, data structures, and LeetCode problem solutions.

## Directory Structure & Conventions

### Core Directories
- `algorithms/` - Fundamental algorithms (BFS, sorting, searching)
- `dataStructures/` - Data structure implementations (BST, LinkedList, Tree)
- `neetcode150/` - LeetCode solutions following NeetCode roadmap (prefixed with problem number)
- `problemSolving/` - General problem solutions, including `LeetCode/` subdirectory

### File Naming Patterns
- Algorithm files: `CamelCaseAlgorithmName.py` (e.g., `BinaryInsertionSort.py`)
- LeetCode problems: `{number}_{snake_case_title}.py` (e.g., `1_Two_Sum.py`)
- Some files use problem numbers only: `1.py`, `101.py`

## Coding Patterns & Conventions

### LeetCode Solutions
- Include full problem description as docstring/comment at top
- Use `class Solution:` pattern for LeetCode problems
- Method signatures match LeetCode exactly (e.g., `def twoSum(self, nums: List[int], target: int) -> List[int]:`)
- Example in `neetcode150/1_Two_Sum.py` and `problemSolving/LeetCode/1.py`

### Data Structures
- Use class-based implementations with descriptive method names
- Follow recursive patterns for tree operations (see `BinarySearchTree.py`)
- Include helper methods like `add_node()`, `search()`, `insertNode()`

### Algorithm Implementations
- Standalone functions with clear parameter names
- Use adjacency list representation for graphs: `adj = {1:[2,3], 2:[1], ...}`
- Include `if __name__ == '__main__':` blocks with test cases
- Example in `algorithms/BFS.py`

### Common Utilities
- Custom swap function using arithmetic: `a=a+b; b=a-b; a=a-b`
- Dictionary-based hashmaps for O(1) lookups
- Iterative and recursive approaches often provided

## Development Workflow

### Running Code
- All files are standalone Python scripts
- Execute with: `python filename.py`
- No external dependencies beyond Python standard library

### Testing Approach
- Most files include basic test cases in `__main__` block
- Manual verification through print statements
- Example test patterns in algorithm files

## Code Quality Guidelines

### When Adding New Solutions
1. Include problem statement/description as comments
2. Match existing naming conventions for the directory
3. Add test cases in `__main__` block for algorithms
4. Use appropriate time/space complexity comments when helpful
5. Follow LeetCode class structure for contest problems

### Data Structure Implementations
- Maintain consistent method naming (`add_node` vs `insert`)
- Include both iterative and recursive approaches where applicable
- Add comprehensive traversal methods (inorder, preorder, postorder)

## Key Files to Reference
- `dataStructures/BinarySearchTree.py` - Class-based data structure pattern
- `algorithms/BFS.py` - Graph algorithm with test case pattern
- `neetcode150/1_Two_Sum.py` - LeetCode problem format with full description
- `problemSolving/AddTwoNumbers.py` - Complex problem with multiple approaches
