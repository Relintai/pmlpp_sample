extends Node

var mlpp_martix_tests : MLPPMatrixTests = null

func _ready() -> void:
	mlpp_martix_tests = MLPPMatrixTests.new()

	mlpp_martix_tests.run_tests()
	
	#mlpp_tests.test_mlpp_matrix()
	#mlpp_tests.test_mlpp_matrix_mul()
	
	get_tree().quit()
