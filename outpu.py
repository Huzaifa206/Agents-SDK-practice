import os
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled
from pydantic import BaseModel,Field
from rich import print

load_dotenv()
set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY")

class name_check(BaseModel):
    is_name:bool =Field(description="if user name is available its value will be true anf if username not available then false")
    username:str=Field(description="username if available,otherwise it will be none")
    age:int=Field(gt=0,description="user age will be in this field")

client=AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

agent = Agent(
    name='Huzaifa',
    instructions='You are a helpful assistant',
    model=OpenAIChatCompletionsModel(
        model='mistralai/mistral-small-24b-instruct-2501',
        openai_client=client
    ),
    output_type=name_check
)

# query=input("User:   ")
Result=Runner.run_sync(starting_agent=agent,input="hi")

print("AI Agent: ",Result.final_output)
print(Result.final_output.is_name)



    # default: Default value if the field is not set.
    #     default_factory: A callable to generate the default value. The callable can either take 0 arguments
    #         (in which case it is called as is) or a single argument containing the already validated data.
    #     alias: The name to use for the attribute when validating or serializing by alias.
    #         This is often used for things like converting between snake and camel case.
    #     alias_priority: Priority of the alias. This affects whether an alias generator is used.
    #     validation_alias: Like `alias`, but only affects validation, not serialization.
    #     serialization_alias: Like `alias`, but only affects serialization, not validation.
    #     title: Human-readable title.
    #     field_title_generator: A callable that takes a field name and returns title for it.
    #     description: Human-readable description.
    #     examples: Example values for this field.
    #     exclude: Whether to exclude the field from the model serialization.
    #     discriminator: Field name or Discriminator for discriminating the type in a tagged union.
    #     deprecated: A deprecation message, an instance of `warnings.deprecated` or the `typing_extensions.deprecated` backport,
    #         or a boolean. If `True`, a default deprecation message will be emitted when accessing the field.
    #     json_schema_extra: A dict or callable to provide extra JSON schema properties.
    #     frozen: Whether the field is frozen. If true, attempts to change the value on an instance will raise an error.
    #     validate_default: If `True`, apply validation to the default value every time you create an instance.
    #         Otherwise, for performance reasons, the default value of the field is trusted and not validated.
    #     repr: A boolean indicating whether to include the field in the `__repr__` output.
    #     init: Whether the field should be included in the constructor of the dataclass.
    #         (Only applies to dataclasses.)
    #     init_var: Whether the field should _only_ be included in the constructor of the dataclass.
    #         (Only applies to dataclasses.)
    #     kw_only: Whether the field should be a keyword-only argument in the constructor of the dataclass.
    #         (Only applies to dataclasses.)
    #     coerce_numbers_to_str: Whether to enable coercion of any `Number` type to `str` (not applicable in `strict` mode).
    #     strict: If `True`, strict validation is applied to the field.
    #         See [Strict Mode](../concepts/strict_mode.md) for details.
    #     gt: Greater than. If set, value must be greater than this. Only applicable to numbers.
    #     ge: Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers.
    #     lt: Less than. If set, value must be less than this. Only applicable to numbers.
    #     le: Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers.
    #     multiple_of: Value must be a multiple of this. Only applicable to numbers.
    #     min_length: Minimum length for iterables.
    #     max_length: Maximum length for iterables.
    #     pattern: Pattern for strings (a regular expression).
    #     allow_inf_nan: Allow `inf`, `-inf`, `nan`. Only applicable to float and [`Decimal`][decimal.Decimal] numbers.
    #     max_digits: Maximum number of allow digits for strings.
    #     decimal_places: Maximum number of decimal places allowed for numbers.
    #     union_mode: The strategy to apply when validating a union. Can be `smart` (the default), or `left_to_right`.
    #         See [Union Mode](../concepts/unions.md#union-modes) for details.
    #     fail_fast: If `True`, validation will stop on the first error. If `False`, all validation errors will be collected.
    #         This option can be applied only to iterable types (list, tuple, set, and frozenset).
    #     extra: (Deprecated) Extra fields that will be included in the JSON schema.

    #         !!! warning Deprecated
    #             The `extra` kwargs is deprecated. Use `json_schema_extra` instead.

    # Returns:
    #     A new [`FieldInfo`][pydantic.fields.FieldInfo]. The return annotation is `Any` so `Field` can be used on
    #         type-annotated fields without causing a type error.
    