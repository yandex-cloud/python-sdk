"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.ai.tuning.v1.tuning_optimizers_pb2
import yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2
import yandex.cloud.ai.tuning.v1.tuning_task_pb2
import yandex.cloud.ai.tuning.v1.tuning_types_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ListTuningsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Required field. ID of the folder to list tunings in."""
    page_size: builtins.int
    """Maximum number of tuning tasks to return per page."""
    page_token: builtins.str
    """Token to retrieve the next page of results."""
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListTuningsRequest = ListTuningsRequest

@typing.final
class ListTuningsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TUNING_TASKS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token to retrieve the next page of results."""
    @property
    def tuning_tasks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.ai.tuning.v1.tuning_task_pb2.TuningTask]:
        """List of tuning tasks in the specified folder."""

    def __init__(
        self,
        *,
        tuning_tasks: collections.abc.Iterable[yandex.cloud.ai.tuning.v1.tuning_task_pb2.TuningTask] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "tuning_tasks", b"tuning_tasks"]) -> None: ...

global___ListTuningsResponse = ListTuningsResponse

@typing.final
class DescribeTuningRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TUNING_TASK_ID_FIELD_NUMBER: builtins.int
    tuning_task_id: builtins.str
    def __init__(
        self,
        *,
        tuning_task_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["tuning_task_id", b"tuning_task_id"]) -> None: ...

global___DescribeTuningRequest = DescribeTuningRequest

@typing.final
class DescribeTuningResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TUNING_TASK_FIELD_NUMBER: builtins.int
    @property
    def tuning_task(self) -> yandex.cloud.ai.tuning.v1.tuning_task_pb2.TuningTask: ...
    def __init__(
        self,
        *,
        tuning_task: yandex.cloud.ai.tuning.v1.tuning_task_pb2.TuningTask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["tuning_task", b"tuning_task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["tuning_task", b"tuning_task"]) -> None: ...

global___DescribeTuningResponse = DescribeTuningResponse

@typing.final
class CancelTuningRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TUNING_TASK_ID_FIELD_NUMBER: builtins.int
    tuning_task_id: builtins.str
    def __init__(
        self,
        *,
        tuning_task_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["tuning_task_id", b"tuning_task_id"]) -> None: ...

global___CancelTuningRequest = CancelTuningRequest

@typing.final
class CancelTuningResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TUNING_TASK_ID_FIELD_NUMBER: builtins.int
    tuning_task_id: builtins.str
    def __init__(
        self,
        *,
        tuning_task_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["tuning_task_id", b"tuning_task_id"]) -> None: ...

global___CancelTuningResponse = CancelTuningResponse

@typing.final
class TuningResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TUNING_TASK_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    TARGET_MODEL_URI_FIELD_NUMBER: builtins.int
    tuning_task_id: builtins.str
    status: yandex.cloud.ai.tuning.v1.tuning_task_pb2.TuningTask.Status.ValueType
    target_model_uri: builtins.str
    def __init__(
        self,
        *,
        tuning_task_id: builtins.str = ...,
        status: yandex.cloud.ai.tuning.v1.tuning_task_pb2.TuningTask.Status.ValueType = ...,
        target_model_uri: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["status", b"status", "target_model_uri", b"target_model_uri", "tuning_task_id", b"tuning_task_id"]) -> None: ...

global___TuningResponse = TuningResponse

@typing.final
class TuningMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TUNING_TASK_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    tuning_task_id: builtins.str
    status: yandex.cloud.ai.tuning.v1.tuning_task_pb2.TuningTask.Status.ValueType
    def __init__(
        self,
        *,
        tuning_task_id: builtins.str = ...,
        status: yandex.cloud.ai.tuning.v1.tuning_task_pb2.TuningTask.Status.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["status", b"status", "tuning_task_id", b"tuning_task_id"]) -> None: ...

global___TuningMetadata = TuningMetadata

@typing.final
class TuningRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class WeightedDataset(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        DATASET_ID_FIELD_NUMBER: builtins.int
        WEIGHT_FIELD_NUMBER: builtins.int
        dataset_id: builtins.str
        weight: builtins.float
        def __init__(
            self,
            *,
            dataset_id: builtins.str = ...,
            weight: builtins.float = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["dataset_id", b"dataset_id", "weight", b"weight"]) -> None: ...

    BASE_MODEL_URI_FIELD_NUMBER: builtins.int
    TRAIN_DATASETS_FIELD_NUMBER: builtins.int
    VALIDATION_DATASETS_FIELD_NUMBER: builtins.int
    TEXT_TO_TEXT_COMPLETION_FIELD_NUMBER: builtins.int
    TEXT_CLASSIFICATION_MULTILABEL_FIELD_NUMBER: builtins.int
    TEXT_CLASSIFICATION_MULTICLASS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    base_model_uri: builtins.str
    """Format like a gpt://{folder_id}/yandex-gpt/latest"""
    name: builtins.str
    """common params"""
    description: builtins.str
    @property
    def train_datasets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TuningRequest.WeightedDataset]: ...
    @property
    def validation_datasets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TuningRequest.WeightedDataset]: ...
    @property
    def text_to_text_completion(self) -> global___TextToTextCompletionTuningParams: ...
    @property
    def text_classification_multilabel(self) -> global___TextClassificationMultilabelParams: ...
    @property
    def text_classification_multiclass(self) -> global___TextClassificationMulticlassParams: ...
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        base_model_uri: builtins.str = ...,
        train_datasets: collections.abc.Iterable[global___TuningRequest.WeightedDataset] | None = ...,
        validation_datasets: collections.abc.Iterable[global___TuningRequest.WeightedDataset] | None = ...,
        text_to_text_completion: global___TextToTextCompletionTuningParams | None = ...,
        text_classification_multilabel: global___TextClassificationMultilabelParams | None = ...,
        text_classification_multiclass: global___TextClassificationMulticlassParams | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["text_classification_multiclass", b"text_classification_multiclass", "text_classification_multilabel", b"text_classification_multilabel", "text_to_text_completion", b"text_to_text_completion", "tuning_params", b"tuning_params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["base_model_uri", b"base_model_uri", "description", b"description", "labels", b"labels", "name", b"name", "text_classification_multiclass", b"text_classification_multiclass", "text_classification_multilabel", b"text_classification_multilabel", "text_to_text_completion", b"text_to_text_completion", "train_datasets", b"train_datasets", "tuning_params", b"tuning_params", "validation_datasets", b"validation_datasets"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["tuning_params", b"tuning_params"]) -> typing.Literal["text_to_text_completion", "text_classification_multilabel", "text_classification_multiclass"] | None: ...

global___TuningRequest = TuningRequest

@typing.final
class TextToTextCompletionTuningParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Scheduler(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        LINEAR_FIELD_NUMBER: builtins.int
        CONSTANT_FIELD_NUMBER: builtins.int
        COSINE_FIELD_NUMBER: builtins.int
        WARMUP_RATIO_FIELD_NUMBER: builtins.int
        warmup_ratio: builtins.float
        @property
        def linear(self) -> yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerLinear: ...
        @property
        def constant(self) -> yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerConstant: ...
        @property
        def cosine(self) -> yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerCosine: ...
        def __init__(
            self,
            *,
            linear: yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerLinear | None = ...,
            constant: yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerConstant | None = ...,
            cosine: yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerCosine | None = ...,
            warmup_ratio: builtins.float = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["constant", b"constant", "cosine", b"cosine", "linear", b"linear", "type", b"type"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["constant", b"constant", "cosine", b"cosine", "linear", b"linear", "type", b"type", "warmup_ratio", b"warmup_ratio"]) -> None: ...
        def WhichOneof(self, oneof_group: typing.Literal["type", b"type"]) -> typing.Literal["linear", "constant", "cosine"] | None: ...

    @typing.final
    class Optimizer(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ADAMW_FIELD_NUMBER: builtins.int
        @property
        def adamw(self) -> yandex.cloud.ai.tuning.v1.tuning_optimizers_pb2.OptimizerAdamw: ...
        def __init__(
            self,
            *,
            adamw: yandex.cloud.ai.tuning.v1.tuning_optimizers_pb2.OptimizerAdamw | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["adamw", b"adamw", "type", b"type"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["adamw", b"adamw", "type", b"type"]) -> None: ...
        def WhichOneof(self, oneof_group: typing.Literal["type", b"type"]) -> typing.Literal["adamw"] | None: ...

    SEED_FIELD_NUMBER: builtins.int
    LR_FIELD_NUMBER: builtins.int
    N_SAMPLES_FIELD_NUMBER: builtins.int
    ADDITIONAL_ARGUMENTS_FIELD_NUMBER: builtins.int
    LORA_FIELD_NUMBER: builtins.int
    PROMPT_TUNE_FIELD_NUMBER: builtins.int
    SCHEDULER_FIELD_NUMBER: builtins.int
    OPTIMIZER_FIELD_NUMBER: builtins.int
    seed: builtins.int
    lr: builtins.float
    n_samples: builtins.int
    additional_arguments: builtins.str
    @property
    def lora(self) -> yandex.cloud.ai.tuning.v1.tuning_types_pb2.TuningTypeLora: ...
    @property
    def prompt_tune(self) -> yandex.cloud.ai.tuning.v1.tuning_types_pb2.TuningTypePromptTune: ...
    @property
    def scheduler(self) -> global___TextToTextCompletionTuningParams.Scheduler: ...
    @property
    def optimizer(self) -> global___TextToTextCompletionTuningParams.Optimizer: ...
    def __init__(
        self,
        *,
        seed: builtins.int = ...,
        lr: builtins.float = ...,
        n_samples: builtins.int = ...,
        additional_arguments: builtins.str = ...,
        lora: yandex.cloud.ai.tuning.v1.tuning_types_pb2.TuningTypeLora | None = ...,
        prompt_tune: yandex.cloud.ai.tuning.v1.tuning_types_pb2.TuningTypePromptTune | None = ...,
        scheduler: global___TextToTextCompletionTuningParams.Scheduler | None = ...,
        optimizer: global___TextToTextCompletionTuningParams.Optimizer | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["lora", b"lora", "optimizer", b"optimizer", "prompt_tune", b"prompt_tune", "scheduler", b"scheduler", "tuning_type", b"tuning_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["additional_arguments", b"additional_arguments", "lora", b"lora", "lr", b"lr", "n_samples", b"n_samples", "optimizer", b"optimizer", "prompt_tune", b"prompt_tune", "scheduler", b"scheduler", "seed", b"seed", "tuning_type", b"tuning_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["tuning_type", b"tuning_type"]) -> typing.Literal["lora", "prompt_tune"] | None: ...

global___TextToTextCompletionTuningParams = TextToTextCompletionTuningParams

@typing.final
class TextClassificationMultilabelParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Scheduler(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        LINEAR_FIELD_NUMBER: builtins.int
        CONSTANT_FIELD_NUMBER: builtins.int
        COSINE_FIELD_NUMBER: builtins.int
        WARMUP_RATIO_FIELD_NUMBER: builtins.int
        warmup_ratio: builtins.float
        @property
        def linear(self) -> yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerLinear: ...
        @property
        def constant(self) -> yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerConstant: ...
        @property
        def cosine(self) -> yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerCosine: ...
        def __init__(
            self,
            *,
            linear: yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerLinear | None = ...,
            constant: yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerConstant | None = ...,
            cosine: yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerCosine | None = ...,
            warmup_ratio: builtins.float = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["constant", b"constant", "cosine", b"cosine", "linear", b"linear", "type", b"type"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["constant", b"constant", "cosine", b"cosine", "linear", b"linear", "type", b"type", "warmup_ratio", b"warmup_ratio"]) -> None: ...
        def WhichOneof(self, oneof_group: typing.Literal["type", b"type"]) -> typing.Literal["linear", "constant", "cosine"] | None: ...

    @typing.final
    class Optimizer(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ADAMW_FIELD_NUMBER: builtins.int
        @property
        def adamw(self) -> yandex.cloud.ai.tuning.v1.tuning_optimizers_pb2.OptimizerAdamw: ...
        def __init__(
            self,
            *,
            adamw: yandex.cloud.ai.tuning.v1.tuning_optimizers_pb2.OptimizerAdamw | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["adamw", b"adamw", "type", b"type"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["adamw", b"adamw", "type", b"type"]) -> None: ...
        def WhichOneof(self, oneof_group: typing.Literal["type", b"type"]) -> typing.Literal["adamw"] | None: ...

    SEED_FIELD_NUMBER: builtins.int
    LR_FIELD_NUMBER: builtins.int
    N_SAMPLES_FIELD_NUMBER: builtins.int
    ADDITIONAL_ARGUMENTS_FIELD_NUMBER: builtins.int
    LORA_FIELD_NUMBER: builtins.int
    PROMPT_TUNE_FIELD_NUMBER: builtins.int
    SCHEDULER_FIELD_NUMBER: builtins.int
    OPTIMIZER_FIELD_NUMBER: builtins.int
    seed: builtins.int
    lr: builtins.float
    n_samples: builtins.int
    additional_arguments: builtins.str
    @property
    def lora(self) -> yandex.cloud.ai.tuning.v1.tuning_types_pb2.TuningTypeLora: ...
    @property
    def prompt_tune(self) -> yandex.cloud.ai.tuning.v1.tuning_types_pb2.TuningTypePromptTune: ...
    @property
    def scheduler(self) -> global___TextClassificationMultilabelParams.Scheduler: ...
    @property
    def optimizer(self) -> global___TextClassificationMultilabelParams.Optimizer: ...
    def __init__(
        self,
        *,
        seed: builtins.int = ...,
        lr: builtins.float = ...,
        n_samples: builtins.int = ...,
        additional_arguments: builtins.str = ...,
        lora: yandex.cloud.ai.tuning.v1.tuning_types_pb2.TuningTypeLora | None = ...,
        prompt_tune: yandex.cloud.ai.tuning.v1.tuning_types_pb2.TuningTypePromptTune | None = ...,
        scheduler: global___TextClassificationMultilabelParams.Scheduler | None = ...,
        optimizer: global___TextClassificationMultilabelParams.Optimizer | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["lora", b"lora", "optimizer", b"optimizer", "prompt_tune", b"prompt_tune", "scheduler", b"scheduler", "tuning_type", b"tuning_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["additional_arguments", b"additional_arguments", "lora", b"lora", "lr", b"lr", "n_samples", b"n_samples", "optimizer", b"optimizer", "prompt_tune", b"prompt_tune", "scheduler", b"scheduler", "seed", b"seed", "tuning_type", b"tuning_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["tuning_type", b"tuning_type"]) -> typing.Literal["lora", "prompt_tune"] | None: ...

global___TextClassificationMultilabelParams = TextClassificationMultilabelParams

@typing.final
class TextClassificationMulticlassParams(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Scheduler(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        LINEAR_FIELD_NUMBER: builtins.int
        CONSTANT_FIELD_NUMBER: builtins.int
        COSINE_FIELD_NUMBER: builtins.int
        WARMUP_RATIO_FIELD_NUMBER: builtins.int
        warmup_ratio: builtins.float
        @property
        def linear(self) -> yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerLinear: ...
        @property
        def constant(self) -> yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerConstant: ...
        @property
        def cosine(self) -> yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerCosine: ...
        def __init__(
            self,
            *,
            linear: yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerLinear | None = ...,
            constant: yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerConstant | None = ...,
            cosine: yandex.cloud.ai.tuning.v1.tuning_schedulers_pb2.SchedulerCosine | None = ...,
            warmup_ratio: builtins.float = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["constant", b"constant", "cosine", b"cosine", "linear", b"linear", "type", b"type"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["constant", b"constant", "cosine", b"cosine", "linear", b"linear", "type", b"type", "warmup_ratio", b"warmup_ratio"]) -> None: ...
        def WhichOneof(self, oneof_group: typing.Literal["type", b"type"]) -> typing.Literal["linear", "constant", "cosine"] | None: ...

    @typing.final
    class Optimizer(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ADAMW_FIELD_NUMBER: builtins.int
        @property
        def adamw(self) -> yandex.cloud.ai.tuning.v1.tuning_optimizers_pb2.OptimizerAdamw: ...
        def __init__(
            self,
            *,
            adamw: yandex.cloud.ai.tuning.v1.tuning_optimizers_pb2.OptimizerAdamw | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["adamw", b"adamw", "type", b"type"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["adamw", b"adamw", "type", b"type"]) -> None: ...
        def WhichOneof(self, oneof_group: typing.Literal["type", b"type"]) -> typing.Literal["adamw"] | None: ...

    SEED_FIELD_NUMBER: builtins.int
    LR_FIELD_NUMBER: builtins.int
    N_SAMPLES_FIELD_NUMBER: builtins.int
    ADDITIONAL_ARGUMENTS_FIELD_NUMBER: builtins.int
    LORA_FIELD_NUMBER: builtins.int
    PROMPT_TUNE_FIELD_NUMBER: builtins.int
    SCHEDULER_FIELD_NUMBER: builtins.int
    OPTIMIZER_FIELD_NUMBER: builtins.int
    seed: builtins.int
    lr: builtins.float
    n_samples: builtins.int
    additional_arguments: builtins.str
    @property
    def lora(self) -> yandex.cloud.ai.tuning.v1.tuning_types_pb2.TuningTypeLora: ...
    @property
    def prompt_tune(self) -> yandex.cloud.ai.tuning.v1.tuning_types_pb2.TuningTypePromptTune: ...
    @property
    def scheduler(self) -> global___TextClassificationMulticlassParams.Scheduler: ...
    @property
    def optimizer(self) -> global___TextClassificationMulticlassParams.Optimizer: ...
    def __init__(
        self,
        *,
        seed: builtins.int = ...,
        lr: builtins.float = ...,
        n_samples: builtins.int = ...,
        additional_arguments: builtins.str = ...,
        lora: yandex.cloud.ai.tuning.v1.tuning_types_pb2.TuningTypeLora | None = ...,
        prompt_tune: yandex.cloud.ai.tuning.v1.tuning_types_pb2.TuningTypePromptTune | None = ...,
        scheduler: global___TextClassificationMulticlassParams.Scheduler | None = ...,
        optimizer: global___TextClassificationMulticlassParams.Optimizer | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["lora", b"lora", "optimizer", b"optimizer", "prompt_tune", b"prompt_tune", "scheduler", b"scheduler", "tuning_type", b"tuning_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["additional_arguments", b"additional_arguments", "lora", b"lora", "lr", b"lr", "n_samples", b"n_samples", "optimizer", b"optimizer", "prompt_tune", b"prompt_tune", "scheduler", b"scheduler", "seed", b"seed", "tuning_type", b"tuning_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["tuning_type", b"tuning_type"]) -> typing.Literal["lora", "prompt_tune"] | None: ...

global___TextClassificationMulticlassParams = TextClassificationMulticlassParams

@typing.final
class GetMetricsUrlRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_ID_FIELD_NUMBER: builtins.int
    task_id: builtins.str
    def __init__(
        self,
        *,
        task_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["task_id", b"task_id"]) -> None: ...

global___GetMetricsUrlRequest = GetMetricsUrlRequest

@typing.final
class GetMetricsUrlResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOAD_URL_FIELD_NUMBER: builtins.int
    load_url: builtins.str
    def __init__(
        self,
        *,
        load_url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["load_url", b"load_url"]) -> None: ...

global___GetMetricsUrlResponse = GetMetricsUrlResponse

@typing.final
class GetOptionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_ID_FIELD_NUMBER: builtins.int
    task_id: builtins.str
    def __init__(
        self,
        *,
        task_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["task_id", b"task_id"]) -> None: ...

global___GetOptionsRequest = GetOptionsRequest

@typing.final
class GetOptionsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_ID_FIELD_NUMBER: builtins.int
    BASE_MODEL_URI_FIELD_NUMBER: builtins.int
    TRAIN_DATASETS_FIELD_NUMBER: builtins.int
    VALIDATION_DATASETS_FIELD_NUMBER: builtins.int
    TEXT_TO_TEXT_COMPLETION_FIELD_NUMBER: builtins.int
    TEXT_CLASSIFICATION_MULTILABEL_FIELD_NUMBER: builtins.int
    TEXT_CLASSIFICATION_MULTICLASS_FIELD_NUMBER: builtins.int
    task_id: builtins.str
    base_model_uri: builtins.str
    @property
    def train_datasets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TuningRequest.WeightedDataset]: ...
    @property
    def validation_datasets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TuningRequest.WeightedDataset]: ...
    @property
    def text_to_text_completion(self) -> global___TextToTextCompletionTuningParams: ...
    @property
    def text_classification_multilabel(self) -> global___TextClassificationMultilabelParams: ...
    @property
    def text_classification_multiclass(self) -> global___TextClassificationMulticlassParams: ...
    def __init__(
        self,
        *,
        task_id: builtins.str = ...,
        base_model_uri: builtins.str = ...,
        train_datasets: collections.abc.Iterable[global___TuningRequest.WeightedDataset] | None = ...,
        validation_datasets: collections.abc.Iterable[global___TuningRequest.WeightedDataset] | None = ...,
        text_to_text_completion: global___TextToTextCompletionTuningParams | None = ...,
        text_classification_multilabel: global___TextClassificationMultilabelParams | None = ...,
        text_classification_multiclass: global___TextClassificationMulticlassParams | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["text_classification_multiclass", b"text_classification_multiclass", "text_classification_multilabel", b"text_classification_multilabel", "text_to_text_completion", b"text_to_text_completion", "tuning_params", b"tuning_params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["base_model_uri", b"base_model_uri", "task_id", b"task_id", "text_classification_multiclass", b"text_classification_multiclass", "text_classification_multilabel", b"text_classification_multilabel", "text_to_text_completion", b"text_to_text_completion", "train_datasets", b"train_datasets", "tuning_params", b"tuning_params", "validation_datasets", b"validation_datasets"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["tuning_params", b"tuning_params"]) -> typing.Literal["text_to_text_completion", "text_classification_multilabel", "text_classification_multiclass"] | None: ...

global___GetOptionsResponse = GetOptionsResponse