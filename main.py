import subprocess
import openai


def run_command(command):
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    if process.returncode != 0:
        raise Exception(f'Command {command} failed with exit code {process.returncode}')
    return process.stdout


def check_if_commits_are_staged():
    try:
        result = run_command('git diff --staged')
        if result == '':
            return False
    except Exception:
        return False
    return True


def generate_commit_message_from_diff(diff):
    prompt = f"""Given the following git patch file:
    {diff}

    ###
    Generate a one-sentence long git commit message.
    Return only the commit message without comments or other text.
    """

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt, temperature=0,
        max_tokens=128)
    message = response['choices'][0]['text']
    return message.strip().replace('"', '').replace("\n", '')


if __name__ == '__main__':
    if not check_if_commits_are_staged():
        print('No staged commits')
        exit(0)
    diff = run_command('git diff --staged')
    commit_message = generate_commit_message_from_diff(diff)
    # run_command(f'git commit -m "{commit_message}"')
    print(f'Committed with message: {commit_message}')