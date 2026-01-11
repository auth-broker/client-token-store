import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedOAuth2Token")


@_attrs_define
class ManagedOAuth2Token:
    """
    Attributes:
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        tenant_id (UUID):
        access_token (str):
        expires_in (int):
        token_type (str):
        created_by (Union[None, UUID, Unset]):
        id (Union[Unset, UUID]):
        name (Union[None, Unset, str]):
        id_token (Union[None, Unset, str]):
        refresh_token (Union[None, Unset, str]):
        scope (Union[None, Unset, str]):
        expires_at (Union[None, Unset, datetime.datetime]):
    """

    updated_at: datetime.datetime
    created_at: datetime.datetime
    tenant_id: UUID
    access_token: str
    expires_in: int
    token_type: str
    created_by: Union[None, UUID, Unset] = UNSET
    id: Union[Unset, UUID] = UNSET
    name: Union[None, Unset, str] = UNSET
    id_token: Union[None, Unset, str] = UNSET
    refresh_token: Union[None, Unset, str] = UNSET
    scope: Union[None, Unset, str] = UNSET
    expires_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        tenant_id = str(self.tenant_id)

        access_token = self.access_token

        expires_in = self.expires_in

        token_type = self.token_type

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        id_token: Union[None, Unset, str]
        if isinstance(self.id_token, Unset):
            id_token = UNSET
        else:
            id_token = self.id_token

        refresh_token: Union[None, Unset, str]
        if isinstance(self.refresh_token, Unset):
            refresh_token = UNSET
        else:
            refresh_token = self.refresh_token

        scope: Union[None, Unset, str]
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

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
                "updated_at": updated_at,
                "created_at": created_at,
                "tenant_id": tenant_id,
                "access_token": access_token,
                "expires_in": expires_in,
                "token_type": token_type,
            }
        )
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if id_token is not UNSET:
            field_dict["id_token"] = id_token
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if scope is not UNSET:
            field_dict["scope"] = scope
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        updated_at = isoparse(d.pop("updated_at"))

        created_at = isoparse(d.pop("created_at"))

        tenant_id = UUID(d.pop("tenant_id"))

        access_token = d.pop("access_token")

        expires_in = d.pop("expires_in")

        token_type = d.pop("token_type")

        def _parse_created_by(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_id_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id_token = _parse_id_token(d.pop("id_token", UNSET))

        def _parse_refresh_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        refresh_token = _parse_refresh_token(d.pop("refresh_token", UNSET))

        def _parse_scope(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scope = _parse_scope(d.pop("scope", UNSET))

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

        managed_o_auth_2_token = cls(
            updated_at=updated_at,
            created_at=created_at,
            tenant_id=tenant_id,
            access_token=access_token,
            expires_in=expires_in,
            token_type=token_type,
            created_by=created_by,
            id=id,
            name=name,
            id_token=id_token,
            refresh_token=refresh_token,
            scope=scope,
            expires_at=expires_at,
        )

        managed_o_auth_2_token.additional_properties = d
        return managed_o_auth_2_token

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
