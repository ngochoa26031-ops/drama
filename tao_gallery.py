import os
from pathlib import Path

def is_image_file(filename):
    ext = Path(filename).suffix.lower()
    return ext in {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.tiff', '.heic', '.avif'}

# Tạo HTML
html_parts = [
    '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📸 Xem Ảnh - Gallery</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f8f9fa; }
        .gallery-img {
            transition: all 0.3s ease;
            cursor: pointer;
            height: 240px;
            object-fit: cover;
        }
        .gallery-img:hover {
            transform: scale(1.08);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        .folder-header {
            border-bottom: 3px solid #0d6efd;
            padding-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container py-5">
        <div class="text-center mb-5">
            <h1 class="display-5 fw-bold">📸 Bộ Sưu Tập Ảnh</h1>
            <p class="text-muted">Click vào ảnh để xem lớn • Hỗ trợ tất cả folder ảnh</p>
        </div>
'''
]

current_dir = Path('.')
folders = sorted([f for f in current_dir.iterdir() if f.is_dir()])

for folder in folders:
    folder_name = folder.name
    images = [f.name for f in folder.iterdir() if f.is_file() and is_image_file(f.name)]
    
    if not images:
        continue
        
    html_parts.append(f'<h2 class="folder-header mt-5 mb-4">📁 {folder_name} <small class="text-muted">({len(images)} ảnh)</small></h2>')
    html_parts.append('<div class="row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-5 g-4">')
    
    for img in sorted(images):
        path = f"{folder_name}/{img}"
        html_parts.append(f'''
        <div class="col">
            <div class="card h-100 border-0 shadow-sm">
                <img src="{path}" class="card-img-top gallery-img" onclick="showImage('{path}', '{img}')" alt="{img}">
                <div class="card-body p-3">
                    <p class="card-text text-truncate small mb-0 text-center">{img}</p>
                </div>
            </div>
        </div>
        ''')
    
    html_parts.append('</div>')

html_parts.extend([
    '''
    </div>

    <!-- Modal xem ảnh lớn -->
    <div class="modal fade" id="imageModal" tabindex="-1">
        <div class="modal-dialog modal-xl modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="modalTitle"></h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body p-2 text-center bg-dark">
                    <img id="modalImage" class="img-fluid" style="max-height: 85vh;" alt="">
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        function showImage(src, filename) {
            const modal = new bootstrap.Modal(document.getElementById('imageModal'));
            document.getElementById('modalImage').src = src;
            document.getElementById('modalTitle').textContent = filename;
            modal.show();
        }
    </script>
</body>
</html>
'''
])

# Ghi file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(html_parts))

print("✅ ĐÃ SỬA XONG! index.html mới đã được tạo.")
print("Mở lại file index.html xem thử, không còn \\n thừa nữa.")