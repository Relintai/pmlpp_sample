extends Node

var mlpp_tests : MLPPMatrixTests = null

func _ready() -> void:
	mlpp_tests = MLPPMatrixTests.new()

	mlpp_tests.test_mlpp_matrix()
	mlpp_tests.test_mlpp_matrix_mul()
