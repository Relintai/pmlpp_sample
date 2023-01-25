extends Node

var mlpp_tests : MLPPTests = null

func _ready() -> void:
	mlpp_tests = MLPPTests.new()
	mlpp_tests.test_statistics()
