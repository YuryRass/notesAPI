from httpx import AsyncClient, Response

from app.notes.router import add_note_for_user, get_notes
from app.utils.url import reverse


async def test_success_add_and_get_note(
    authenticated_ac: AsyncClient, true_content: str
) -> None:
    response: Response = await authenticated_ac.post(
        url=reverse(add_note_for_user),
        json={"content": true_content},
    )

    assert response.status_code == 200

    response: Response = await authenticated_ac.get(url=reverse(get_notes))

    assert response.status_code == 200
    assert response.json()[-1]["content"] == true_content


async def test_unsuccess_add_note(
    authenticated_ac: AsyncClient, invalid_content: str
) -> None:
    response: Response = await authenticated_ac.post(
        url=reverse(add_note_for_user),
        json={"content": invalid_content},
    )

    assert response.status_code == 422
