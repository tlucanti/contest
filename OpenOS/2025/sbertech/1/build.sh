#!/bin/bash

rpm -qa --qf '%{NAME}-%{VERSION}-%{RELEASE}.%{ARCH}\n' > "rpm.txt"
rpm -qa --qf '%{NAME}-%{VERSION}-%{RELEASE}.src.rpm\n' >> "srpm.txt"

echo "" > "rpm.yaml"
echo "" > "srpm.yaml"

while IFS= read -r pkg; do
    echo "Processing: $pkg"

    echo "$pkg:" >> "rpm.yaml"

    deps=$(rpm -qR "$pkg" 2>/dev/null || true)

    echo "$deps" | while IFS= read -r dep; do
        if rpm -q --whatprovides "$dep" >/dev/null 2>/dev/null; then
            echo "  - $dep" >> "rpm.yaml"
        fi
    done

done < "rpm.txt"

while IFS= read -r pkg; do
    echo "Processing: $pkg"

    base_name=$(echo "$pkg" | sed 's/\.src\.rpm$//')
    echo "$base_name:" >> "srpm.yaml"

    deps=$(rpm -q --requires "$pkg" 2>/dev/null || true)

    echo "$deps" | while IFS= read -r dep; do
        if rpm -q --whatprovides "$dep" >/dev/null 2>/dev/null; then
            echo "  - $dep" >> "srpm.yaml"
        fi
    done

done < "srpm.txt"


sed -i '/^$/d' "srpm.yaml"
sed -i '/^$/d' "rpm.yaml"

rm "rpm.txt"
rm "srpm.txt"
