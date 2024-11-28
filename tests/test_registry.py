from models.registry import RegistryModel


def test_registry_model_initialization():
    url = "http://test-registry"
    username = "test_user"
    password = "test_pass"

    model = RegistryModel(url, username, password)

    assert model.url == url
    assert model.username == username
    assert model.password == password
