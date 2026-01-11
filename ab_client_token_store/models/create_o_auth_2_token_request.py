import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_2_token import OAuth2Token


T = TypeVar("T", bound="CreateOAuth2TokenRequest")


@_attrs_define
class CreateOAuth2TokenRequest:
    """
    Attributes:
        created_by (UUID):
        tenant_id (UUID):
        oauth2_token (OAuth2Token): An OAuth2 token model with secrets stored as SecretStr.
        name (Union[None, Unset, str]):
        expires_at (Union[None, Unset, datetime.datetime]):
    """

    created_by: UUID
    tenant_id: UUID
    oauth2_token: "OAuth2Token"
    name: Union[None, Unset, str] = UNSET
    expires_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = str(self.created_by)

        tenant_id = str(self.tenant_id)

        oauth2_token = self.oauth2_token.to_dict()

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "tenant_id": tenant_id,
                "oauth2_token": oauth2_token,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_2_token import OAuth2Token

        d = dict(src_dict)
        created_by = UUID(d.pop("created_by"))

        tenant_id = UUID(d.pop("tenant_id"))

        oauth2_token = OAuth2Token.from_dict(d.pop("oauth2_token"))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_expires_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        create_o_auth_2_token_request = cls(
            created_by=created_by,
            tenant_id=tenant_id,
            oauth2_token=oauth2_token,
            name=name,
            expires_at=expires_at,
        )

        create_o_auth_2_token_request.additional_properties = d
        return create_o_auth_2_token_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
