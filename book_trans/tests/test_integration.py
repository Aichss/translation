import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture()
def test_book_dir() -> str:

    return str(Path(__file__).parent.parent / "test_books")

def test_openai_translate_epub_zh_hans(test_book_dir, tmpdir):
    shutil.copyfile(
        os.path.join(test_book_dir, "lemo.epub"),
        os.path.join(tmpdir, "lemo.epub"),
    )

    subprocess.run(
        [
            sys.executable,
            "make_book.py",
            "--book_name",
            os.path.join(tmpdir, "lemo.epub"),
            "--test",
            "--test_num",
            "5",
            "--language",
            "zh-hans",
        ],
        env=os.environ.copy(),
    )
    assert os.path.isfile(os.path.join(tmpdir, "lemo_bilingual.epub"))
    assert os.path.getsize(os.path.join(tmpdir, "lemo_bilingual.epub")) != 0


@pytest.mark.skipif(
    not os.environ.get("OPENAI_API_KEY"),
    reason="No OPENAI_API_KEY in environment variable.",
)
def test_openai_translate_epub_ja_prompt_txt(test_book_dir, tmpdir):
    shutil.copyfile(
        os.path.join(test_book_dir, "animal_farm.epub"),
        os.path.join(tmpdir, "animal_farm.epub"),
    )

    subprocess.run(
        [
            sys.executable,
            "make_book.py",
            "--book_name",
            os.path.join(tmpdir, "animal_farm.epub"),
            "--test",
            "--test_num",
            "5",
            "--language",
            "ja",
            "--model",
            "gpt3",
            "--prompt",
            "prompt_template_sample.txt",
        ],
        env=os.environ.copy(),
    )
    assert os.path.isfile(os.path.join(tmpdir, "animal_farm_bilingual.epub"))
    assert os.path.getsize(os.path.join(tmpdir, "animal_farm_bilingual.epub")) != 0


@pytest.mark.skipif(
    not os.environ.get("OPENAI_API_KEY"),
    reason="No OPENAI_API_KEY in environment variable.",
)
def test_openai_translate_epub_ja_prompt_json(test_book_dir, tmpdir):
    shutil.copyfile(
        os.path.join(test_book_dir, "animal_farm.epub"),
        os.path.join(tmpdir, "animal_farm.epub"),
    )

    subprocess.run(
        [
            sys.executable,
            "make_book.py",
            "--book_name",
            os.path.join(tmpdir, "animal_farm.epub"),
            "--test",
            "--test_num",
            "5",
            "--language",
            "ja",
            "--prompt",
            "prompt_template_sample.json",
        ],
        env=os.environ.copy(),
    )
    assert os.path.isfile(os.path.join(tmpdir, "animal_farm_bilingual.epub"))
    assert os.path.getsize(os.path.join(tmpdir, "animal_farm_bilingual.epub")) != 0


@pytest.mark.skipif(
    not os.environ.get("OPENAI_API_KEY"),
    reason="No OPENAI_API_KEY in environment variable.",
)
def test_openai_translate_srt(test_book_dir, tmpdir):
    shutil.copyfile(
        os.path.join(test_book_dir, "Lex_Fridman_episode_322.srt"),
        os.path.join(tmpdir, "Lex_Fridman_episode_322.srt"),
    )

    subprocess.run(
        [
            sys.executable,
            "make_book.py",
            "--book_name",
            os.path.join(tmpdir, "Lex_Fridman_episode_322.srt"),
            "--test",
            "--test_num",
            "20",
        ],
        env=os.environ.copy(),
    )
    assert os.path.isfile(os.path.join(tmpdir, "Lex_Fridman_episode_322_bilingual.srt"))
    assert (
        os.path.getsize(os.path.join(tmpdir, "Lex_Fridman_episode_322_bilingual.srt"))
        != 0
    )
