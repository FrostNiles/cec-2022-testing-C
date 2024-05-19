### Testing CEC benchmark 2022 C version of code 

Testing CEC benchmark 2022 from https://github.com/P-N-Suganthan/2022-SO-BO

The codes could be found in https://github.com/P-N-Suganthan/2022-SO-BO/blob/main/CEC2022.zip

The raw codes were taken there and modified for testing purposes.

### Running the tests

To run tests check combine-dim-func.py where you set number of functions i, dimensions j, and number of element k.

Test run is paralel for all the functions.

For manual testing check run-tests.py. It is possilbe to run this script with arguments number of function, dimension and number of element.

### Making graphs and tables

To differ languages use lang-comparison.py, final-graph.py and before that get-lowest-deviation.py. The modification of these scripts are required the paths would be different.

To get all the tables and graphs for all the elements of functions in all dimensions in different languages use plot-graph.py. Here it would be required to change the paths.

### Results

Results are find in test_data/result

### portability

It is possilbe to run all the tests in different years, just check the years documentation, change mains so it writes results in appropriate files.

Change the precission - it is now to 10e-08 in every document, it is possilbe to change it globally one day not now. (seven digits now in scripts.py and 9 floating point numbers in mains)

First try run-tests.py for single element few times.

Lastly change the combine-dim-func.py so you can run it automatically for the years functions.