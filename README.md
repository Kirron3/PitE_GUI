# Data Visualizer (PitE Project)

A GUI application developed as part of the Programming in the Enterprise (PitE) course that allows users to visualize data through an interactive interface. The application is built with Python and Tkinter, providing a user-friendly way to analyze and plot data from various file formats.

## Project Goals

- Build an interactive GUI application using Tkinter
- Enable users to explore and analyze data through visual representations
- Provide a flexible and user-friendly interface for data visualization

## Features

### File Browser
- Load data from multiple file formats (CSV, TXT, Excel)
- Display selected file path in the GUI
- Preview file contents in a structured table format

### Data Preview
- Interactive table view showing the first few rows of data
- Column headers clearly displayed
- Scrollable preview for larger datasets

### Plotting Options
- Dynamic column selection for X and Y axes via dropdown menus
- Multiple plot types available:
  - Line plots
  - Scatter plots
  - Bar charts
- Customizable plot settings

### Plot Display
- Embedded Matplotlib figure within the Tkinter GUI
- Interactive navigation toolbar with zoom and pan capabilities
- Responsive plot rendering

### Error Handling
- Graceful handling of invalid file formats
- User prompts for missing or invalid selections
- Clear error messages and guidance

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Kirron3/PitE_GUI.git
```

2. Install required dependencies:
```bash
pip install pandas matplotlib
```

3. Run the application:
```bash
python GUI.py
```

## Future Enhancements

### Advanced Features
- Support for additional file formats (HDF, JSON)
- Data filtering and aggregation capabilities
- Enhanced interactive features for plots
- Customizable bin contents for histograms

### Planned Improvements
- Advanced data preprocessing options
- Multiple plot windows
- Custom plot styling options
- Data export capabilities

## Project Structure
```
PitE_GUI/
├── GUI.py    # Main application file
├── README.md            # Project documentation
└── test.csv         # file to test code

## Contributing

This project is part of the PitE course but welcomes contributions. Some areas where you can contribute:
- Adding support for new file formats
- Implementing additional plot types
- Improving the user interface
- Adding data preprocessing features
- Enhancing error handling
