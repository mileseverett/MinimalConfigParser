import inspect
import yaml


def class_init_args_to_dict(cls):
    init_signature = inspect.signature(cls.__init__)
    init_args = {}

    for name, param in init_signature.parameters.items():
        if name != "self" and param.default != inspect.Parameter.empty:
            init_args[name] = param.default

    return init_args


def generate_yaml_from_class(cls, yaml_file_path):
    class_path = f"{cls.__module__}.{cls.__name__}"
    init_args = class_init_args_to_dict(cls)

    config = {"class_path": class_path, "init_args": init_args}

    with open(yaml_file_path, "w") as file:
        yaml.dump(config, file)


from models.ExpandableMLP import ExpandableMLPLM

if __name__ == "__main__":
    generate_yaml_from_class(ExpandableMLPLM, "generated_config.yaml")
