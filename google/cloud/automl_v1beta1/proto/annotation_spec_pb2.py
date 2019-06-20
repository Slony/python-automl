# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/annotation_spec.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/annotation_spec.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1"
    ),
    serialized_pb=_b(
        '\n7google/cloud/automl_v1beta1/proto/annotation_spec.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto"K\n\x0e\x41nnotationSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x15\n\rexample_count\x18\t \x01(\x05\x42\x84\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1b\x06proto3'
    ),
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)


_ANNOTATIONSPEC = _descriptor.Descriptor(
    name="AnnotationSpec",
    full_name="google.cloud.automl.v1beta1.AnnotationSpec",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.automl.v1beta1.AnnotationSpec.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.automl.v1beta1.AnnotationSpec.display_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="example_count",
            full_name="google.cloud.automl.v1beta1.AnnotationSpec.example_count",
            index=2,
            number=9,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=118,
    serialized_end=193,
)

DESCRIPTOR.message_types_by_name["AnnotationSpec"] = _ANNOTATIONSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnnotationSpec = _reflection.GeneratedProtocolMessageType(
    "AnnotationSpec",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ANNOTATIONSPEC,
        __module__="google.cloud.automl_v1beta1.proto.annotation_spec_pb2",
        __doc__="""A definition of an annotation spec.
  
  
  Attributes:
      name:
          Output only. Resource name of the annotation spec. Form:  'pro
          jects/{project\_id}/locations/{location\_id}/datasets/{dataset
          \_id}/annotationSpecs/{annotation\_spec\_id}'
      display_name:
          Required. The name of the annotation spec to show in the
          interface. The name can be up to 32 characters long and must
          match the regexp ``[a-zA-Z0-9_]+``. (\_), and ASCII digits
          0-9.
      example_count:
          Output only. The number of examples in the parent dataset
          labeled by the annotation spec.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.AnnotationSpec)
    ),
)
_sym_db.RegisterMessage(AnnotationSpec)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
