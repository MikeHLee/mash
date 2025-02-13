import click
from typing import Optional
from .models import get_model_handler

@click.group()
def cli():
    """MASH - Master Shell for interacting with various LLM providers"""
    pass

@cli.command()
@click.argument('question', type=str)
@click.option('--model', '-m', default='gpt4', type=click.Choice(['gpt4', 'claude', 'ollama']),
              help='The model to use for generating the response')
def ask(question: str, model: Optional[str] = 'gpt4'):
    """Ask a question to the specified LLM model"""
    try:
        model_handler = get_model_handler(model)
        for chunk in model_handler.stream_response(question):
            click.echo(chunk, nl=False)
        click.echo()
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    cli()
