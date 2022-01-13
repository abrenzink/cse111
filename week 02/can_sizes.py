import math

def main():

    name = "#1 Picnic"
    radius = 6.83	
    height = 10.16
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name}: {round(storage_efficiency, 2)}")

    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name}: {round(storage_efficiency, 2)}")

    name = "#2"
    radius = 8.73
    height = 11.59
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name}: {round(storage_efficiency, 2)}")

    name = "#2.5"
    radius = 10.32
    height = 11.91
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name}: {round(storage_efficiency, 2)}")

    name = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name}: {round(storage_efficiency, 2)}")

    name = "#5"
    radius = 13.02
    height = 14.29
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name}: {round(storage_efficiency, 2)}")

    name = "#6Z"
    radius = 5.4
    height = 8.89
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name}: {round(storage_efficiency, 2)}")

    name = "#8Z short"
    radius = 6.83
    height = 7.62
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name}: {round(storage_efficiency, 2)}")

    name = "#10"
    radius = 15.72
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name}: {round(storage_efficiency, 2)}")

    name = "#211"
    radius = 6.83
    height = 12.38
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name}: {round(storage_efficiency, 2)}")

    name = "#300"
    radius = 7.62
    height = 11.27
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name}: {round(storage_efficiency, 2)}")

    name = "#303"
    radius = 8.1
    height = 11.11
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name}: {round(storage_efficiency, 2)}")

def compute_volume(r, h):
    volume = math.pi * r * r * h
    return volume 

def compute_surface_area(r, h):
    surface_area = 2 * math.pi * r * (r + h)
    return surface_area

def compute_storage_efficiency(v, sa):
    storage_efficiency = v/sa
    return storage_efficiency

main()