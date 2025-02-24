
import pytest
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from invoices.extract_cufe import create_database, extract_cufe


@pytest.fixture(scope="module")
def setup_database():
    create_database()
    yield

@pytest.fixture
def sample_pdf_with_cufe(tmp_path):
    pdf_path = tmp_path / "sample.pdf"
    cufe = "f2e7a47d940438ab9fdbd8e1d30b8b7431bf8cddf328b6726d1b5bba9180e0f6194fb8e5770abe45485560ef7083ad87"

    c = canvas.Canvas(str(pdf_path), pagesize=letter)
    c.drawString(100, 750, f"CUFE: {cufe}")
    c.save()

    return str(pdf_path), cufe


@pytest.fixture
def sample_pdf_without_cufe(tmp_path):
    pdf_path = tmp_path / "sample.pdf"
    c = canvas.Canvas(str(pdf_path), pagesize=letter)
    c.drawString(100, 750, "Este PDF no contiene un CUFE válido.")
    c.save()

    return str(pdf_path)

def test_extract_cufe_without_cufe(sample_pdf_without_cufe):
    nombre, paginas, cufe, peso = extract_cufe(sample_pdf_without_cufe)
    assert nombre == "sample.pdf"
    assert paginas == 1
    assert cufe == "No encontrado"
    assert peso > 0

def test_extract_cufe_with_cufe(sample_pdf_with_cufe):
    pdf_path, expected_cufe = sample_pdf_with_cufe
    nombre, paginas, cufe, peso = extract_cufe(pdf_path)
    assert nombre == "sample.pdf"
    assert paginas == 1
    assert cufe == expected_cufe
    assert peso > 0
