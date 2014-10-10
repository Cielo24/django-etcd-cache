import os


def get_dot_env(base_dir):
    dot_env = os.path.join(base_dir, '.env')
    if os.path.exists(dot_env):
        _env = {}
        with open(dot_env, 'rb') as fh:
            for line in fh.readlines():
                line = line.strip()
                if line == '':
                    continue

                # ignore comments
                if line.startswith('#'):
                    continue

                _, kv = line.split(' ', 1)
                k, v = kv.split('=')

                if v.startswith('"') or v.startswith("'"):
                    v = v[1:-1]

                _env[k] = v
        os.environ.update(_env)
