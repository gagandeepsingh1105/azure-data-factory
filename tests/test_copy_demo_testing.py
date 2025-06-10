import pytest
import os
from data_factory_testing_framework import TestFramework, TestFrameworkType
from data_factory_testing_framework.models import Pipeline
from data_factory_testing_framework.state import PipelineRunState, RunParameter, RunParameterType

@pytest.fixture
def test_framework(request) -> TestFramework:
    return TestFramework(
            framework_type = TestFrameworkType.DataFactory,
            root_folder_path = os.path.join(request.fspath.dirname, '..', 'pipeline')

@pytest.fixture
def pipeline(test_framework) -> Pipeline:
    return(test_framework.get_pipeline_by_name('copy_demo_testing')

def validate_sink_folder(pipeline) -> None:
    # Arrange
    activity = pipeline.get_activity_by_name('Copy data1')
    run_state = PipelineRunState(
                    parameters = [
                                    RunParameter(RunParameterType.Pipeline, name="p_sink_folder", value="target")
                                  ]
                                  )
                    

    # Act
    activity.evaluate(run_state)

    # Assert
    output_dataset = activity.outputs[0]
    assert output_dataset.parameters["p_directory"].result == 'target'
