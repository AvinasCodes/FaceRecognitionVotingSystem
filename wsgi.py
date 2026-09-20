import os
import sys

# Compatibility shim: face_recognition_models depends on pkg_resources,
# which was deprecated/removed in newer setuptools releases.
try:
    import pkg_resources
except ImportError:
    import importlib.util
    class _PkgResourcesShim:
        @staticmethod
        def resource_filename(package_or_requirement, resource_name):
            if isinstance(package_or_requirement, str):
                spec = importlib.util.find_spec(package_or_requirement)
                if spec and spec.origin:
                    base_dir = os.path.dirname(spec.origin)
                    return os.path.join(base_dir, resource_name)
            return resource_name
    sys.modules['pkg_resources'] = _PkgResourcesShim()

from app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)